%define oname pymagic
%define sover 1

Name: python3-module-%oname
Version: 1.0
Release: alt3.1

Summary: libmagic bindings
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/libmagic/

Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libmagic-devel

%py3_provides %oname

%if "%_lib" == "lib64"
Requires: libmagic.so.%sover()(64bit)
%else
Requires: libmagic.so.%sover
%endif


%description
libmagic bindings using FFL (ctypes).

%prep
%setup
%patch0 -p2

%build
%python3_build_debug

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
   %buildroot%python3_sitelibdir
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%if 0
%__python3 pymagic.py pymagic.py
%endif

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Wed Jan 15 2020 Ivan A. Melnikov <iv@altlinux.org> 1.0-alt3.1
- use correct dependency on all 32-bit platforms

* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt3
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Fixed build

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

