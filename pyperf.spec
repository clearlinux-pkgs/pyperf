#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyperf
Version  : 2.3.0
Release  : 20
URL      : https://files.pythonhosted.org/packages/63/b9/af915e7bb6a12bc5fa990a70bad9945490547158dd66ed10cb877cb8ef42/pyperf-2.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/63/b9/af915e7bb6a12bc5fa990a70bad9945490547158dd66ed10cb877cb8ef42/pyperf-2.3.0.tar.gz
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
******
pyperf
******
.. image:: https://img.shields.io/pypi/v/pyperf.svg
:alt: Latest release on the Python Cheeseshop (PyPI)
:target: https://pypi.python.org/pypi/pyperf

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
%setup -q -n pyperf-2.3.0
cd %{_builddir}/pyperf-2.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632868748
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyperf
cp %{_builddir}/pyperf-2.3.0/COPYING %{buildroot}/usr/share/package-licenses/pyperf/0c885fb5d06bf65019b498d9cef9641983dd58ad
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
