%global pypi_name python-editor

%define with_python3 1

Name: python-module-editor
Version: 0.4
Release: alt1.1.1

Summary: Programmatically open an editor, capture the result

License: ASL 2.0
Group: Development/Python
Url: https://github.com/fmoo/python-editor

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://pypi.python.org/packages/source/p/%pypi_name/%pypi_name-%version.tar.gz

BuildArch: noarch

#BuildPreReq: rpm-build-python3 python3-module-distribute

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools

%description
An python module which provides a convenient example.

%if 0%with_python3
%package -n python3-module-editor
Summary: Programmatically open an editor, capture the result
#BuildRequires: python3-devel
Group: Development/Python

%description -n python3-module-editor
An python module which provides a convenient example.
%endif

%prep
%setup -n %pypi_name-%version
rm -rf %pypi_name.egg-info

%build
%python_build
%if 0%with_python3
%python3_build
%endif

%install
%python_install
chmod a+x %buildroot%python_sitelibdir/editor.py

%if 0%with_python3
%python3_install
chmod a+x %buildroot%python3_sitelibdir/editor.py
%__subst "s|python$|python3|g" %buildroot%python3_sitelibdir/editor.py
%endif

%check

%files
%doc README.md
%doc LICENSE
%python_sitelibdir/editor.py*
%python_sitelibdir/python_editor-%version-py?.?.egg-info

%if 0%with_python3
%files -n python3-module-editor
%doc README.md
%doc LICENSE
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/editor.py*
#python3_sitelibdir/__pycache__/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- initial build for ALT Linux Sisyphus

* Wed Aug 26 2015 Lukas Bezdicka <lbezdick@redhat.com> - 0.4-1
- Bump to 0.4

* Tue Aug 25 2015 Lukas Bezdicka <lbezdick@redhat.com> - 0.3-1
- initial package
