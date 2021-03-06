#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyperf
Version  : 2.2.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/f5/15/e055fca622a985602df49e9afabd73c093cced18e0283c06918400fd196a/pyperf-2.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/15/e055fca622a985602df49e9afabd73c093cced18e0283c06918400fd196a/pyperf-2.2.0.tar.gz
Summary  : Python module to run and analyze benchmarks
Group    : Development/Tools
License  : MIT
Requires: pyperf-bin = %{version}-%{release}
Requires: pyperf-license = %{version}-%{release}
Requires: pyperf-python = %{version}-%{release}
Requires: pyperf-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
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

%description python3
python3 components for the pyperf package.


%prep
%setup -q -n pyperf-2.2.0
cd %{_builddir}/pyperf-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1625012293
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyperf
cp %{_builddir}/pyperf-2.2.0/COPYING %{buildroot}/usr/share/package-licenses/pyperf/0c885fb5d06bf65019b498d9cef9641983dd58ad
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
