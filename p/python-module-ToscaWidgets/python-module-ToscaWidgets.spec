%define srcname ToscaWidgets

Name: python-module-ToscaWidgets
Version: 0.9.10
Release: alt1.1

Summary: Toolkit to help create widgets for WSGI web apps

Group: Development/Python
License: MIT
Url: http://toscawidgets.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/T/%srcname/%srcname-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools

%setup_python_module tw

%description
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the web.

ToscaWidgets is an almost complete rewrite of the widgets package bundled with
TurboGears-1.0. The rewrite's goal was to decouple the widgets package from
CherryPy and TurboGears itself to fit better with TurboGears 2.0
philosophy which is to partition it's services into independent WSGI
components for easier mainteinance and reuse in other Python web applications
or frameworks.

%prep
%setup -n %srcname-%version

%build
%python_build

%install
%python_install
install -m644 tw/__init__.py %buildroot/%python_sitelibdir/%modulename/

%files
%doc README.txt PKG-INFO
%python_sitelibdir/%modulename/
%python_sitelibdir/%srcname-*.egg-info
%python_sitelibdir/%srcname-*-nspkg.pth

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.10-alt1.1
- Rebuild with Python-2.7

* Tue Oct 05 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.10-alt1
- initial build for ALT Linux Sisyphus

* Wed Jul 28 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 26 2010 Luke Macken <lmacken@redhat.com> - 0.9.10-1
- 0.9.10 bugfix release
- Remove python-toscawidgets-deprecation.patch

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Wed Jan 27 2010 Luke Macken <lmacken@redhat.com> - 0.9.9-1
- 0.9.9 release
- Update the deprecation warning patch

* Sun Nov 29 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.8-2
- Fix deprecation warnings

* Thu Oct 01 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-1
- 0.9.8 release
- Remove js patch which is now upstream

* Thu Aug 27 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-0.4.dev20090825
- Apply a patch from http://toscawidgets.org/trac/tw/ticket/30
  to fix problems with encoding javascript methods.

* Tue Aug 25 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-0.3.dev20090825
- Update to the latest mercurial snapshot, which fixes the python 2.4
  incompatibilites.

* Mon Aug 24 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-0.2.dev20090822
- Add a couple of patches to get things working on Python2.4

* Sat Aug 22 2009 Luke Macken <lmacken@redhat.com> - 0.9.8-0.1.dev20090822
- Update to a 0.9.8 development snapshot

* Wed Aug 12 2009 Luke Macken <lmacken@redhat.com> - 0.9.7.2-1
- 0.9.7.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 27 2009 Luke Macken <lmacken@redhat.com> - 0.9.7.1-1
- 0.9.7.1
- s/define/global/

* Thu Jun 04 2009 Luke Macken <lmacken@redhat.com> - 0.9.6-1
- Update to 0.9.6

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Luke Macken <lmacken@redhat.com> - 0.9.4-1
- Update to 0.9.4

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.3-2
- Rebuild for Python 2.6

* Tue Aug 26 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.3-1
- New upstream.

* Sun Jul 27 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.2-2
- Require python-webob

* Mon Jul 07 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.2-1
- Update to latest release.
- Fixes problem with pages being returned as text/plain.

* Mon Jun 02 2008 Luke Macken <lmacken@redhat.com> - 0.9.1-1
- Update to latest release
- Remove python-paste-script, python-ruledispatch, python-decorator and
  python-decoratortools dependencies.

* Sat May 31 2008 Luke Macken <lmacken@redhat.com> - 0.8.7-1
- Update to latest release.

* Fri May 30 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.8.6.1-1
- Update to latest release.

* Thu Mar 20 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-0.3.20080320svn4283
- Update to a snapshot.

* Thu Dec 20 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-0.2.rc3dev_r3795
- Add Requires

* Wed Dec 19 2007 Toshio Kuratomi <toshio@fedoraproject.org> - 0.2-0.1.rc3dev_r3795
- Inital Fedora Build
