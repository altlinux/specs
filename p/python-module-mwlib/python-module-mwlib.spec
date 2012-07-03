%define modulename mwlib

Name: python-module-mwlib
Version: 0.12.16
Release: alt2.1.1

Summary: MediaWiki conversion library for Python

Group: Development/Python
License: BSD
Url: http://code.pediapress.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildPreReq: rpm-build-python

%setup_python_module %modulename

# Write manually:
BuildPreReq: gcc-c++ re2c python-devel >= 2.5 python-module-docutils
BuildPreReq: python-module-flup python-module-odfpy
BuildPreReq: python-module-pyparsing python-module-simplejson python-module-imaging
Requires: python-module-twisted-core >= 8.2.0 python-module-twisted-web >= 8.2.0
Requires: python-module-flup >= 1.0 python-module-qserve

%description
mwlib is a Python library for parsing MediaWiki articles. It is
currently aimed at developers, who have a need to somehow handle
MediaWiki articles.

%define mwserve_log    %_logdir/mwserve
%define mwserve_cache  %_cachedir/mwserve
%define mwserve_piddir %_runtimedir/mwserve
%define mwserve_user   mwserve
%define mwserve_group  mwserve

%prep
%setup

%build
%python_build
%__make -C docs

%install
%python_install
install %modulename/__init__.* %buildroot%python_sitelibdir/%modulename/
#install daemon stuff
mkdir -p -- %buildroot/%_initdir %buildroot/%_sysconfdir/logrotate.d
mkdir -p -- %buildroot/%mwserve_log %buildroot/%mwserve_cache %buildroot/%mwserve_piddir
install -m 0755 -- mwserve.init %buildroot%_initdir/mwserve
install -m 0640 -- mwserve.logrotate %buildroot%_sysconfdir/logrotate.d/mwserve

%pre
# Add the "mwserve" user
%_sbindir/groupadd -r -f %mwserve_group 2>/dev/null ||:
%_sbindir/useradd  -r -g %mwserve_group -c 'mwlib server daemon' \
       -s /dev/null -d %mwserve_cache %mwserve_user 2>/dev/null ||:

%post
%post_service mwserve

%preun
%preun_service mwserve


%files
%doc README.txt docs/*.{txt,html}
%python_sitelibdir/mwlib*
%python_sitelibdir/argv.*
%_bindir/*
%config    %_initdir/mwserve
%attr(640,root,root) %config %_sysconfdir/logrotate.d/mwserve
%attr(0770,root,%mwserve_group) %dir %mwserve_log
%attr(0770,root,%mwserve_group) %dir %mwserve_cache
%attr(0770,root,%mwserve_group) %dir %mwserve_piddir


%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.16-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.16-alt2.1
- Rebuild with Python-2.7

* Fri Oct 21 2011 Michael A. Kangin <prividen@altlinux.org> 0.12.16-alt2
- 0.12.16 alt2 release

* Fri Oct 14 2011 Vitaly Lipatov <lav@altlinux.ru> 0.12.16-alt1
- new version 0.12.16 (with rpmrb script)

* Thu Jul 15 2010 Michael A. Kangin <prividen@altlinux.org> 0.12.12-alt3
- Support for mwserve daemon

* Tue Jun 22 2010 Michael A. Kangin <prividen@altlinux.org> 0.12.12-alt2
- Fix requires (Closes: #23146)

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.12.12-alt1
- new version (0.12.12) import in git

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-3.20090522hg2956
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Ian Weller <ian@ianweller.org> - 0.11.2-2.20090522hg2956
- odfpy07 does not exist

* Fri May 22 2009 Ian Weller <ianweller@gmail.coM> - 0.11.2-1.20090522hg2956
- Bump to hg tip which fixes bug 486678

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 Ian Weller <ianweller@gmail.com> 0.9.10-1
- Bump to 0.9.10

* Sat Feb 14 2009 Ian Weller <ianweller@gmail.com> 0.9.7-1
- Bump to 0.9.7

* Mon Jan 26 2009 Ian Weller <ianweller@gmail.com> 0.9.5-1
- Bump to 0.9.5
- F8 is EOL, remove F8-specific requires

* Wed Dec 17 2008 Ian Weller <ianweller@gmail.com> 0.9.2-1
- Bump to 0.9.2

* Thu Oct 23 2008 Ian Weller <ianweller@gmail.com> 0.8.5-1
- Bump to 0.8.5

* Fri Aug 22 2008 Ian Weller <ianweller@gmail.com> 0.8.3-1
- Bump to 0.8.3

* Mon Aug 04 2008 Ian Weller <ianweller@gmail.com> 0.8.1-1
- Bump to 0.8.1

* Thu Jul 31 2008 Paul W. Frields <stickster@gmail.com> - 0.8.0-3
- Fix Requires to unbreak F-8 dependencies

* Fri Jul 25 2008 Ian Weller <ianweller@gmail.com> 0.8.0-2
- Fix source URL (again)
- Remove make commands because setup.py build does that now
- Kill off the check section
- Fix license

* Mon Jul 21 2008 Ian Weller <ianweller@gmail.com> 0.8.0-1
- Bump to 0.8.0

* Sun Jul 13 2008 Ian Weller <ianweller@gmail.com> 0.7.1-1
- Fix source URL, license, other things

* Sun Jul 13 2008 Paul W. Frields <stickster@gmail.com> - 0.7.1-0.1
- Initial RPM package
