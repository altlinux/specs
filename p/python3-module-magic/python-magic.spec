%define oname python-magic
%define sover 1

Name: python3-module-magic
Version: 0.4.25
Release: alt1

Summary: File type identification using libmagic

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-magic/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%py3_provides %oname
Provides: python3-module-libmagic = %EVR
Obsoletes: python3-module-libmagic

Requires: %_libdir/libmagic.so.%sover

%description
This module uses ctypes to access the libmagic file type identification
library. It makes use of the local magic database and supports both
textual and MIME-type output.

%prep
%setup
#sed -i "s|@64@|%_libsuff|" magic.py
#sed -i "s|@SOVER@|%sover|" magic.py

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%if "%_lib" == "lib64"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
# TODO
#export LC_ALL=en_US.UTF-8
#python3 setup.py test || :

%files
%doc *.md
%python3_sitelibdir/*

%changelog
* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 0.4.25-alt1
- new version 0.4.25 (with rpmrb script)

* Sun Aug 29 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4.24-alt1
- new version 0.4.24 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4.22-alt1
- new version 0.4.22 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4.13-alt3
- build python3 package separately, under more correct name

* Mon Feb 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.13-alt2
- fixed build on aarch64

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.13-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.13-alt1
- Updated to upstream version 0.4.13.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.6-alt1.git20150107.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1.git20150107.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20150107
- New snapshot

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20141111
- Initial build for Sisyphus

