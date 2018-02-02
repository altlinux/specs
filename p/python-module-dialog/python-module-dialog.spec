%global upstream_name pythondialog
%global upstream_name2 python2-pythondialog

%def_with python3

Name: python-module-dialog
Version: 3.3.0
Release: alt1.1.1

Summary: Python interface to the Unix dialog utility

License: LGPLv2+
Group: Development/Python
Url: http://pythondialog.sourceforge.net
# Upstream releases two tarballs from the same sources
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: https://pypi.python.org/packages/source/p/%upstream_name/%upstream_name-%version.tar
Source1: https://pypi.python.org/packages/source/p/%upstream_name2/%upstream_name2-%version.tar

BuildArch: noarch
BuildRequires: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-setuptools
%endif

%description
A Python interface to the Unix dialog utility, designed to provide an
easy, pythonic and as complete as possible way to use the dialog
features from Python code.

%if_with python3
%package -n python3-module-dialog
Requires: dialog
Summary: %summary
Group: Development/Python

%description -n python3-module-dialog
A Python interface to the Unix dialog utility, designed to provide an
easy, pythonic and as complete as possible way to use the dialog
features from Python code.
%endif

%prep
%setup -n %upstream_name-%version
tar -xvf %SOURCE1

%build
%if_with python3
%python3_build
%endif

pushd %upstream_name2-%version
%python_build
popd

%install
%if_with python3
%python3_install
%endif

pushd %upstream_name2-%version
%python_install
popd

%if_with python3
%files -n python3-module-dialog
%doc COPYING
%doc README.rst examples/
%python3_sitelibdir/dialog.py*
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/pythondialog-*.egg-info
%endif

%files
%doc %upstream_name2-%version/COPYING
%doc %upstream_name2-%version/README.rst %upstream_name2-%version/examples/
%python_sitelibdir/dialog.py*
%python_sitelibdir/python2_pythondialog-*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.3.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 16 2016 Vitaly Lipatov <lav@altlinux.ru> 3.3.0-alt1
- initial build for ALT Linux Sisyphus

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 12 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.3.0-7
- Restore %%license
- Simplify spec file

* Sat Dec 12 2015 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.3.0-6
- include python_provide macro bz# 1291005
- include el6 conditionals / fixes from Nick Le Mouton

* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 3.3.0-5
- epel7: Only build python2 package

* Thu Dec 03 2015 Robert Buchholz <rbu@goodpoint.de> - 3.3.0-4
- No need to convert README, upstream provides utf-8
- Remove obsolete comment

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 12 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@laptop> - 3.3.0-1
- Add python3 subpackage

* Wed Oct 28 2015 Felix Schwarz <fschwarz@fedoraproject.org> - 3.3.0-1
- update to new upstream version (#998103)
- drop patch for demo.py (included in upstream release)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 20 2011 Miloš Jakubíček <xjakub@fi.muni.cz> - 2.7-13
- Added python-dialog-demo.patch, fix BZ#594988
- Fix rpmlint: W: file-not-utf8 /usr/share/doc/python-dialog-2.7/TODO
- Fix rpmlint: W: file-not-utf8 /usr/share/doc/python-dialog-2.7/README

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.7-9
- Rebuild for Python 2.6

* Thu Jun 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 2.7-8
- add egg info

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.7-7
- fix license tag (see head of dialog.py)

* Sat Dec 09 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.7-6
- rebuild

* Wed Nov 01 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.7-5
- unghost .pyo file

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 2.7-4
- rebuild

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 2.7-3
- rebuild for FC5

* Fri Dec 23 2005 Aurelien Bompard <gauret[AT]free.fr> 2.7-1
- remove hardcoded disttag

* Wed Mar 30 2005 Aurelien Bompard <gauret[AT]free.fr> 2.7-1.fc4
- change release tag for FC4
- drop Epoch

* Thu Feb 10 2005 Aurelien Bompard <gauret[AT]free.fr> 0:2.7-1
- update to version 2.7
- update URL

* Sat Feb 05 2005 Toshio Kuratomi <toshio@tiki-lounge.com> 0:2.0.6-2
- Change %%python_sitearch to %%python_sitelib as sitearch references
  /usr/lib64 on x86_64 multilib and the python files install to /usr/lib.

* Sat Jul 24 2004 Aurelien Bompard <gauret[AT]free.fr> 0:2.06-0.fdr.1
- Initial Fedora Package
