Name: rpm-build-xdg
Version: 0.2
Release: alt1

Summary: RPM macros for XDG Base Directory Specification and more
License: %gpl3plus
Group: Development/Other
Url: http://standards.freedesktop.org/basedir-spec/

Packager: Alexey Rusakov <ktirf@altlinux.org>

BuildArch: noarch

BuildPreReq: rpm-build-licenses

%description
This package contains RPM macros that correspond to standard values defined
in XDG Base Directory Specification and other specifications that reference
this. Note that these macros do not replace values of environment variables
that are defined in the Specification, they just set some default paths
that are used for packaging XDG-compliant software.

%install
cat <<__EOF__ >xdg.rpmmacros
%%_xdgdatadir %%_datadir
%%_xdgmimedir %%_xdgdatadir/mime
%%_xdgconfigdir %%_sysconfdir/xdg
%%_xdgmenusdir %%_xdgconfigdir/menus
__EOF__
install -D -m644 xdg.rpmmacros %buildroot/%_rpmmacrosdir/xdg

%files
%_rpmmacrosdir/xdg

%changelog
* Sat Aug 15 2009 Alexey Rusakov <ktirf@altlinux.org> 0.2-alt1
- Added %%_xdgmenusdir macro.

* Wed Jun 03 2009 Alexey Rusakov <ktirf@altlinux.org> 0.1-alt1.1
- Fixed the Summary.

* Mon Jun 01 2009 Alexey Rusakov <ktirf@altlinux.org> 0.1-alt1
- Initial Sisyphus release.

