%define _name python-distutils-extra
%define ver_major 2.38

Name: python-module-distutils-extra
Version: %ver_major
Release: alt1.1

Summary: Integrate more support into Python's distutils
Group: Development/Python
License: GPLv2+
Url: https://launchpad.net/%_name
Packager: Paul Wolneykien <manowar@altlinux.ru>

Source: http://launchpad.net/%_name/trunk/%ver_major/+download/%_name-%version.tar.gz

BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools rpm-build-python
#BuildPreReq: python3-devel python3-module-setuptools rpm-build-python3

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3

%description
Enables you to easily integrate gettext support, themed icons and
documentation into Python's distutils.

%package -n python3-module-distutils-extra
Summary: Integrate more support into Python3 distutils
Group: Development/Python3

%description -n python3-module-distutils-extra
Enables you to easily integrate gettext support, themed icons and
documentation into Python3 distutils.


%prep
%setup -n %_name-%version -a0
mv %_name-%version py3build

%build
%python_build
pushd py3build
%python3_build
popd

%install
%python_install

pushd py3build
%python3_install
popd

chmod a+x %buildroot{%python_sitelibdir,%python3_sitelibdir}/DistUtilsExtra/command/build_extra.py

%files
%doc doc/*
%python_sitelibdir/DistUtilsExtra/
%python_sitelibdir/python_distutils_extra*.egg-info

%files -n python3-module-distutils-extra
%doc doc/*
%python3_sitelibdir/DistUtilsExtra/
%python3_sitelibdir/python_distutils_extra*.egg-info


%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.38-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 24 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38-alt1
- 2.38
- new python3 module

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.29-alt1.1
- Rebuild with Python-2.7

* Sat Oct 01 2011 Andrey Cherepanov <cas@altlinux.org> 2.29-alt1
- New verion 2.29

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1.1
- Rebuilt with python 2.6

* Fri Aug 04 2009 Paul Wolneykien <manowar@altlinux.ru> 2.6-alt1
- Initial build for ALTLinux

* Sat Aug 01 2009 Fabian Affolter <fabian@bernewireless.net> - 2.6-2
- Bump release

* Sat Aug 01 2009 Fabian Affolter <fabian@bernewireless.net> - 2.6-1
- Minor spec file changes
- Changed source to launchpad
- Updated to new upstream version 2.6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.91.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Fabian Affolter <fabian@bernewireless.net> - 1.91.2-2
- Changed license to GPLv2+

* Sat Nov 18 2008 Fabian Affolter <fabian@bernewireless.net> - 1.91.2-1
- Initial package for Fedora

