%add_findreq_skiplist %_datadir/%name/*
%add_python_req_skip cvstoys

Name: buildbot
Version: 0.7.12
Release: alt2.1
Summary: Build/test automation system

Group: Development/Python
License: GPLv2+
Url: http://buildbot.net
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel

%description
The BuildBot is a system to automate the compile/test cycle required by
most software projects to validate code changes. By automatically
rebuilding and testing the tree each time something has changed, build
problems are pinpointed quickly, before other developers are
inconvenienced by the failure.

%package contrib
Summary: Contribs for %name
Group: Development/Python

%description contrib
Additional scripts for %name

%prep
%setup

%build
%python_build

%install

%python_install --install-purelib=%python_sitelibdir

mkdir -p %buildroot/%_datadir/%name/
cp -R contrib %buildroot/%_datadir/%name/

# clean up Windows contribs.
sed -i 's/\r//' %buildroot/%_datadir/%name/contrib/windows/*
chmod -x %buildroot/%_datadir/%name/contrib/windows/*

%files
%doc NEWS README docs
%_bindir/buildbot
%python_sitelibdir/buildbot
%python_sitelibdir/*.egg-info

%files contrib
%_datadir/%name

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.12-alt2.1
- Rebuild with Python-2.7

* Mon May 30 2011 Alexey Shabalin <shaba@altlinux.ru> 0.7.12-alt2
- add contrib to skip list

* Sat Feb 06 2010 Boris Savelev <boris@altlinux.org> 0.7.12-alt1
- new version

* Thu Nov 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.11p3-alt2.1
- Rebuilt with python 2.6

* Fri Nov 13 2009 Boris Savelev <boris@altlinux.org> 0.7.11p3-alt2
- move contrib to subpackage (closes: #22277)

* Mon Oct 12 2009 Boris Savelev <boris@altlinux.org> 0.7.11p3-alt1
- new version

* Mon Oct 01 2009 Boris Savelev <boris@altlinux.org> 0.7.10p1-alt1
- initial build for Sisyphus

* Thu Sep 10 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.7.10p1-2mdv2010.0
+ Revision: 436903
- rebuild

* Thu Mar 05 2009 Jérôme Soyer <saispo@mandriva.org> 0.7.10p1-1mdv2009.1
+ Revision: 348914
- New upstream release

* Sun Dec 28 2008 Funda Wang <fundawang@mandriva.org> 0.7.9-1mdv2009.1
+ Revision: 320366
- New version 0.7.9

* Mon Aug 11 2008 Jérôme Soyer <saispo@mandriva.org> 0.7.8-1mdv2009.0
+ Revision: 270612
- New release 0.7.8

* Thu Aug 07 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.7.7-2mdv2009.0
+ Revision: 266429
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Funda Wang <fundawang@mandriva.org> 0.7.7-1mdv2009.0
+ Revision: 195060
- New version 0.7.7

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 09 2007 Jérôme Soyer <saispo@mandriva.org> 0.7.6-1mdv2008.1
+ Revision: 95946
- New release 0.7.6
- New release 0.7.6

* Thu Sep 27 2007 Anne Nicolas <anne.nicolas@mandriva.com> 0.7.5-3mdv2008.0
+ Revision: 93423
- bump release to reupload

* Wed Jun 06 2007 Jérôme Soyer <saispo@mandriva.org> 0.7.5-2mdv2008.0
+ Revision: 36098
- Fix %%mkrel number
- Bump release for rebuild
- Remove noarch
- Fix 64bits Build
- Fix RPM Group
- Import buildbot

