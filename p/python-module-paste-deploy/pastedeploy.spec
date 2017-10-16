%define oname paste-deploy

%def_with python3

Name:           python-module-%oname
Version:        1.5.2
Release:        alt1
Summary:        Load, configure, and compose WSGI applications and servers
Group:          Development/Python
License:        MIT
URL:            https://pypi.python.org/pypi/PasteDeploy
BuildArch:      noarch

Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
%endif

%description
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files.  PasteScript provides commands to serve applications based on
this configuration file.

%if_with python3
%package -n python3-module-%oname
Summary:        Load, configure, and compose WSGI applications and servers
Group:          Development/Python3

%description -n python3-module-%oname
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files.  PasteScript provides commands to serve applications based on
this configuration file.
%endif

%prep
%setup

# Remove bundled egg-info if it exists
rm -rf *.egg-info

mv docs/license.txt license.txt

%if_with python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
rm -rf %buildroot%python_sitelibdir/test

%if_with python3
pushd ../python3
%python3_install
rm -rf %buildroot%python3_sitelibdir/test
popd
%endif

%files
%doc docs/* license.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc docs/* license.txt
%python3_sitelibdir/*
%endif

%changelog
* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.2-alt1
- Initial build for ALT.

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 1.5.2-12
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.2-9
- Rebuild for Python 3.6

* Mon Dec 05 2016 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.5.2-8
- Use the Python provides macro to make a python-2 subpackage (#1399573).
- Mark license.txt as a license.
- Depend on python3-paste and remove a no-longer-correct comment.
- Move BuildRequires to top.
- Create global for description and summary.
- Don't remove the buildroot at the beginning of install.
- Drop defattr from the files section.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Feb 12 2014 Ralph Bean <rbean@redhat.com> - 1.5.2-1
- Latest upstream.

* Mon Aug 19 2013 Ralph Bean <rbean@redhat.com> - 1.5.0-10
- Fix typo in with_python3 conditional; patch from Tomas Dabašinskas.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Ralph Bean <rbean@redhat.com> - 1.5.0-8
- Removed extra dependency on python3-paste.

* Wed Feb 27 2013 Ralph Bean <rbean@redhat.com> - 1.5.0-7
- Added python3 subpackage.
- Corrected pythonsitelib typo in %%install section.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 26 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5.0-4
- Add dependency on python-setuptools since parts of paste.deploy rely on
  pkg_resources

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 11 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 1.5.0-2
- Remove the test directory as it serves no purpose and pollutes the global namespace
  https://bugzilla.redhat.com/show_bug.cgi?id=720055

* Thu Jun 16 2011 Luke Macken <lmacken@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 30 2010 Luke Macken <lmacken@redhat.com> - 1.3.4-1
- Update to 1.3.4

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jan 28 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 1.3.3-2
- Modernise the build

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Luke Macken <lmacken@redhat.com> - 1.3.3-1
- Update to 1.3.3

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.3.2-2
- Rebuild for Python 2.6

* Sat Jun 14 2008 Luke Macken <lmacken@redhat.com> - 1.3.2-3
- Update to PasteDeploy 1.3.2

* Sun Sep  2 2007 Luke Macken <lmacken@redhat.com> - 1.3.1-2
- Update for python-setuptools changes in rawhide

* Sun Jul  8 2007 Luke Macken <lmacken@redhat.com> - 1.3.1-1
- 1.3.1

* Sat Mar  3 2007 Luke Macken <lmacken@redhat.com> - 1.1-1
- 1.1

* Sat Dec  9 2006 Luke Macken <lmacken@redhat.com> - 1.0-2
- Add python-devel to BuildRequires
- 1.0

* Sun Sep 17 2006 Luke Macken <lmacken@redhat.com> - 0.9.6-1
- 0.9.6

* Sun Sep  3 2006 Luke Macken <lmacken@redhat.com> - 0.5-4
- Rebuild for FC6

* Mon Aug 21 2006 Luke Macken <lmacken@redhat.com> - 0.5-3
- Include .pyo files instead of ghosting them.

* Mon Jul 24 2006 Luke Macken <lmacken@redhat.com> - 0.5-2
- Fix docs inclusion
- Rename package to python-paste-deploy
- Fix inconsistent use of buildroots

* Mon Jul 10 2006 Luke Macken <lmacken@redhat.com> - 0.5-1
- Initial package
