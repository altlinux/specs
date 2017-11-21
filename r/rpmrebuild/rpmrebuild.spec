Name: rpmrebuild
Version: 2.11
Release: alt3
License: GPLv2+
Group: Development/Other
Summary: A tool to build rpm file from rpm database
Source: %name-%version.tar.gz
Patch: rpmrebuild-2.9-alt-tmpdir.patch
Patch1: rpmrebuild-2.11-alt-toonewtags.patch
Patch2: rpmrebuild-2.11-correctly-quote-rpmargs.patch
Patch3: rpmrebuild-alt-remove-SendBugReport.patch
Url: http://rpmrebuild.sourceforge.net/
BuildArch: noarch

Requires: /usr/bin/rpmbuild
# due to rpmrebuild.sh
Requires: setarch

%description
Rpmrebuild is a tool to build an RPM file from a package that has
already been installed in a basic use, rpmrebuild use do not require any
rpm building knowledge (On debian, the equivalent product is
dpkg-repack)

%package un_prelink
Group: Development/Other
Summary: An prelink -u plugin for %name
Requires: %name = %version-%release

%description un_prelink
Rpmrebuild plugin for automatically un-prelinking package content.

%prep
%setup -c %name-%version
%patch -p2
%patch1 -p1
%patch2 -p2
%patch3 -p2

%build
%make

%install
%makeinstall_std

%find_lang --with-man --output %name.lang ".*"

%files -f %name.lang
%doc Changelog News README Release Todo VERSION Version
%exclude %_man1dir/un_prelink.plug*
%exclude %_mandir/*/*/un_prelink.plug*
%exclude %prefix/lib/%name/plugins/un_prelink*

%_bindir/*
%dir %prefix/lib/%name
%prefix/lib/%name/*
%_man1dir/*

%files un_prelink
%_man1dir/un_prelink.plug*
%_mandir/*/*/un_prelink.plug*
%prefix/lib/%name/plugins/un_prelink*

%changelog
* Tue Nov 21 2017 Dmitry V. Levin <ldv@altlinux.org> 2.11-alt3
- Removed unused SendBugReport to get rid of /bin/mail dependence
  (suggested by Ivan Zakharyaschev).

* Mon May 15 2017 Ivan Zakharyaschev <imz@altlinux.org> 2.11-alt2
- Correctly quote the values passed to --define
- Rebuild to get correct deps on prelink-tools (without prelink cronjob)

* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 2.11-alt1
- Autobuild version bump to 2.11
- ALT-unsupported tags removel updated

* Tue Aug 27 2013 Fr. Br. George <george@altlinux.ru> 2.10-alt2
- Revert ALT-unsupported tags check

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 2.10-alt1
- Autobuild version bump to 2.10

* Mon Apr 01 2013 Fr. Br. George <george@altlinux.ru> 2.9-alt2
- Fix ~/.tmp usage
- Add plugin manpages

* Thu Feb 14 2013 Fr. Br. George <george@altlinux.ru> 2.9-alt1
- Autobuild version bump to 2.9

* Sun Jul 22 2012 Fr. Br. George <george@altlinux.ru> 2.8-alt1
- Autobuild version bump to 2.8

* Tue Jun 19 2012 Dmitry V. Levin <ldv@altlinux.org> 2.7-alt2
- Fixed package requirements.

* Mon Jun 18 2012 Fr. Br. George <george@altlinux.ru> 2.7-alt1
- Autobuild version bump to 2.7
- Separate package requiring prelink

* Tue Aug 16 2011 Fr. Br. George <george@altlinux.ru> 2.6-alt1
- Autobuild version bump to 2.6

* Sat Apr 16 2011 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Initial build from scratch

