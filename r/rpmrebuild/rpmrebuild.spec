Name: rpmrebuild
Version: 2.21
Release: alt2
License: GPL-2.0+
Group: Development/Other
Summary: A tool to build rpm file from rpm database
Source: %name-%version.tar.gz
Patch0: rpmrebuild-2.21-alt-tmpdir.patch
Patch1: rpmrebuild-2.21-correctly-quote-rpmargs.patch
Patch2: rpmrebuild-2.21-optional-man.patch
Patch3: rpmrebuild-alt-remove-SendBugReport.patch
Patch4: rpmrebuild-2.21-optional-rpm2archive.patch
Patch5: rpmrebuild-2.21-plugin-dir-before-options.patch
Url: http://rpmrebuild.sourceforge.net/

BuildArch: noarch

Requires: /usr/bin/rpmbuild
# due to rpmrebuild.sh
Requires: setarch

%description
Rpmrebuild is a tool to build an RPM file from a package that has
already been installed in a basic use, rpmrebuild use do not require any
rpm building knowledge (On debian, the equivalent product is
dpkg-repack).

%prep
%setup -c %name-%version
%patch0 -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2

%build
%make

%install
%makeinstall_std
/bin/rm %buildroot%_man1dir/un_prelink.plug* \
        %buildroot%_mandir/*/*/un_prelink.plug* \
        %buildroot%_libexecdir/%name/plugins/un_prelink*
%find_lang --with-man --output %name.lang ".*"

%files -f %name.lang
%doc Changelog News README Release Todo
%_bindir/*
%dir %prefix/lib/%name
%prefix/lib/%name/*
%_man1dir/*

%changelog
* Wed Oct 21 2026 Anton Farygin <rider@altlinux.org> 2.21-alt2
- Initialize plugin directory before parsing options to fix rpmrebuild-arepo.
- Remove dependencies on optional tools to reduce arepo chroot size (ALT #61153).
- Restore removal of SendBugReport.

* Mon Oct 19 2026 Andrey Cherepanov <cas@altlinux.org> 2.21-alt1
- New version (ALT #35167).
- Removed rpmrebuild-un_prelink (ALT #56683).

* Wed Nov 18 2020 Dmitry V. Levin <ldv@altlinux.org> 2.11-alt6
- rpmrebuild: fixed handling of more than 9 arguments.

* Wed Oct 02 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.11-alt5
- Package %name-un_prelink subpackage only on architectures supported
  by prelink.

* Tue Oct 30 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.11-alt4
- Reintroduced disttag (rediffed rpmrebuild-2.11-alt-toonewtags.patch).

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

