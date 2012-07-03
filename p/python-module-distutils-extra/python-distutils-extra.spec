Name:           python-module-distutils-extra
Version:        2.29
Release:        alt1.1
Summary:        Integrate more support into Python's distutils
Packager:       Paul Wolneykien <manowar@altlinux.ru>

Group:          Development/Python
License:        GPLv2+
URL:            https://launchpad.net/python-distutils-extra
Source0:        http://launchpad.net/%{name}/trunk/2.29/+download/%{name}-%{version}.tar.gz

BuildPreReq:    python-devel python-module-setuptools rpm-build-python

BuildArch:      noarch

%description
Enables you to easily integrate gettext support, themed icons and
scrollkeeper based documentation into Python's distutils.

%prep
%setup -q

%build
%python_build

%install
%python_install
chmod a+x %{buildroot}%{python_sitelibdir}/DistUtilsExtra/command/build_extra.py

%files
%defattr(-,root,root,-)
%doc LICENSE doc/*
%{python_sitelibdir}/DistUtilsExtra/
%{python_sitelibdir}/python_distutils_extra*.egg-info


%changelog
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

