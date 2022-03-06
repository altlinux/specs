%define oname pyramid

%def_without bootstrap

Name:           python3-module-%oname
Version:        2.0
Release:        alt1
Summary:        The Pyramid web application framework, a Pylons project
Group:          Development/Python3
License:        BSD
URL:            https://trypyramid.com/
BuildArch:      noarch

# https://github.com/Pylons/pyramid.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3(chameleon) python3(mako) python3(repoze.lru)
BuildRequires: python3(venusian) python3(webtest) python3(zope.deprecation)
BuildRequires: python3(docutils) python3(hupper) python3(paste.deploy)
BuildRequires: python3(plaster) python3(plaster_pastedeploy) python3(sphinx)
BuildRequires: python3(translationstring) python3(zope.component) python3(zope.configuration)
BuildRequires: python3(zope.interface) python3(webob)

%py3_requires paste.deploy plaster_pastedeploy

%if_with bootstrap
# break cyclic dependency on bootstrap
%add_python3_req_skip pyramid_zodbconn
%endif

Conflicts: python3-module-%oname =< %version-release

%description
Pyramid is a small, fast, down-to-earth, open source Python web development
framework. It makes real-world web application development and deployment more
fun, more predictable, and more productive.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc README.rst LICENSE.txt
%python3_sitelibdir/%oname/
%python3_sitelibdir/%{oname}-%{version}*.egg-info
%_bindir/pdistreport
%_bindir/prequest
%_bindir/proutes
%_bindir/pserve
%_bindir/pshell
%_bindir/ptweens
%_bindir/pviews

%changelog
* Sun Jan 30 2022 Anton Midyukov <antohami@altlinux.org> 2.0-alt1
- new version 2.0
- build python3 module only

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt2.qa1
- NMU: applied repocop patch

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.1-alt2
- Rebuilt without bootstrap.

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.9.1-alt1
- Initial build for ALT.

* Sat Sep 16 2017 Kevin Fenzi <kevin@scrye.com> - 1.9.1-1
- Update to 1.9.1. Fixes bug #1471097

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.9-1
- Update to 1.9 (#1465428).
- https://docs.pylonsproject.org/projects/pyramid/en/1.9-branch/changes.html
- Remove deprecated python3-* executables.
- Refactor the symlink code to use a for loop for simplicity.

* Sat Jul 01 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.8.4-2
- Use python2- versions of dependencies, where available.

* Sat Jul 01 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.8.4-1
- Update to 1.8.4.
- https://docs.pylonsproject.org/projects/pyramid/en/1.8-branch/changes.html#id1
- Mark the LICENSE.txt with the license macro.
- Spice up the Source0 URL so it puts the name in the source tarball.
- Use the correct URL.
- Provide a python2-pyramid package.
- Provide the correct executable names for the python2- and python3- subpackages.
- Leave old python3- executables for the time being, even though they are not the correct names.
- Sort dependencies lexigraphically.

* Sat Mar 25 2017 Kevin Fenzi <kevin@scrye.com> - 1.8.3-1
- Update to 1.8.3. Fixes bug #1431609

* Fri Mar 10 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.8.2-2
- Depend on python{2,3}-hupper (#1431289).

* Tue Feb 21 2017 Kevin Fenzi <kevin@scrye.com> - 1.8.2-1
- Update to 1.8.2. Fixes bug #1413949

* Sun Feb 19 2017 Kevin Fenzi <kevin@scrye.com> - 1.8.1-1
- Update to 1.8.1. Fixes bug #1413949

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.6-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 15 2015 Ralph Bean <rbean@redhat.com> - 1.5.6-1
- new version

* Wed Apr 15 2015 Ralph Bean <rbean@redhat.com> - 1.5.1-2
- Upstream epel7 to 1.5.1.

* Fri Nov 07 2014 Ralph Bean <rbean@redhat.com> - 1.4.6-1
- Upstream 1.4.6 for epel7.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Dec 06 2013 Pierre-Yves Chibon <pingou@pingoured>fr - 1.4-11
- Change BR from python-setuptools-devel to python-setuptools
  See https://fedoraproject.org/wiki/Changes/Remove_Python-setuptools-devel

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 16 2013 Ralph Bean <rbean@redhat.com> - 1.4-9
- Make python-webob dependency contingent on f19.

* Tue Apr 16 2013 Ralph Bean <rbean@redhat.com> - 1.4-8
- Explicitly copy scaffolds into buildroot.
- More explicit file ownership.

* Fri Apr  5 2013 Luke Macken <lmacken@redhat.com> - 1.4-7
- Require python-webob >= 1.2 instead of the python-webob1.2 package

* Wed Feb 27 2013 Ralph Bean <rbean@redhat.com> - 1.4-6
- Reenabled the python3 subpackage.
- Correctly prefixed python3 executables.
- Remove egg-info in prep, not after build.

* Fri Feb 22 2013 Ralph Bean <rbean@redhat.com> - 1.4-5
- Manually disabled python3 subpackage; waiting on deps.
- Loosened constraint on python-webob version.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Ralph Bean <rbean@redhat.com> - 1.4-3
- Packaged python3 subpackage.
- Removed unnecessary Buildroot tag.
- Removed requirement on python-virtualenv.
- Removed requirement on python-paste.

* Mon Dec 31 2012 Ralph Bean <rbean@redhat.com> - 1.4-2
- Add zope.interface to the setuptools hack for el6.
- Add dep on python-unittest2 for el6.
- Add dep on python-ordereddict for el6.
- Remove bundled egg-info
- More specific directory listing in python_sitelib.
- Disable tests for el6.  Unexplained failure.

* Wed Dec 19 2012 Ralph Bean <rbean@redhat.com> - 1.4-1
- Latest upstream.

* Mon Dec 10 2012 Ralph Bean <rbean@redhat.com> - 1.4b3-1
- Latest upstream.  1.4b2-1 was a brownbag release.

* Mon Dec 10 2012 Ralph Bean <rbean@redhat.com> - 1.4b2-1
- Latest upstream.

* Wed Nov 28 2012 Ralph Bean <rbean@redhat.com> - 1.4b1-1
- Latest upstream.
- Removed unnecessary defattr and clean section.
- Re-enabled test suite/check section.
- Removed old patch.
- Depend on and force python-webob1.2
- A bunch of new _bindir tools.

* Wed Oct 10 2012 Tomas Dabasinskas <tomas@redhat.com> - 1.2.7-6
- Changed python-mako requires. 
  For rhel python-mako0.4, else python-mako >= 0.3.6

* Wed Sep 26 2012 Tomas Dabasinskas <tomas@redhat.com> - 1.2.7-5
- Added patch to change install requires from python-paste-script >= 1.7.4
  to python-paste-script >= 1.7.3, python-paste-script is provided by Red Hat
  patch applied if running on rhel
- Added version numbers for required packages
  
* Wed Sep 26 2012 Tomas Dabasinskas <tomas@redhat.com> - 1.2.7-4
- For requires, changed python-webob package to python-webob1.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Ross Delinger <rossdylan@csh.rit.edu> - 1.2-1
- Updated to upstream version 1.2.7
- Disabled unit tests because of false negatives, will be renabled for the 1.3.x
  release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 18 2011 Luke Macken <lmacken@redhat.com> - 1.1.2-1
- Latest upstream release
- Update our requirements

* Sat Jan  2 2010 Luke Macken <lmacken@redhat.com> - 1.0-1
- Initial package
