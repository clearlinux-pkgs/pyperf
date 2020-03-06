#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyperf
Version  : 1.7.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/04/6a/8efd2be0f883e5cef006db69e14224b49b2df57633b759ee5c8fee9f3017/pyperf-1.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/04/6a/8efd2be0f883e5cef006db69e14224b49b2df57633b759ee5c8fee9f3017/pyperf-1.7.0.tar.gz
Summary  : Python module to run and analyze benchmarks
Group    : Development/Tools
License  : MIT
Requires: pyperf-bin = %{version}-%{release}
Requires: pyperf-license = %{version}-%{release}
Requires: pyperf-python = %{version}-%{release}
Requires: pyperf-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
pyperf
        ******

%package bin
Summary: bin components for the pyperf package.
Group: Binaries
Requires: pyperf-license = %{version}-%{release}

%description bin
bin components for the pyperf package.


%package license
Summary: license components for the pyperf package.
Group: Default

%description license
license components for the pyperf package.


%package python
Summary: python components for the pyperf package.
Group: Default
Requires: pyperf-python3 = %{version}-%{release}

%description python
python components for the pyperf package.


%package python3
Summary: python3 components for the pyperf package.
Group: Default
Requires: python3-core
Provides: pypi(pyperf)
Requires: pypi(six)

%description python3
python3 components for the pyperf package.


%prep
%setup -q -n pyperf-1.7.0
cd %{_builddir}/pyperf-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583533655
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyperf
cp %{_builddir}/pyperf-1.7.0/COPYING %{buildroot}/usr/share/package-licenses/pyperf/0c885fb5d06bf65019b498d9cef9641983dd58ad
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyperf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyperf/0c885fb5d06bf65019b498d9cef9641983dd58ad

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
