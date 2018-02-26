Name: thunar-plugger
Version: 1.3
Release: alt1
Summary: Thunar-plugger is a wrapper to run the Thunar plugins

Group:     Graphical desktop/Other
License:   %gpl3plus
URL:	   http://git.altlinux.org/people/manowar/packages/thunar-plugger.git
Source:   %name-%version.tar

Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-xfce4 xfce4-dev-tools
BuildPreReq: libThunar-devel

%description
Thunar-plugger is a standalone application which is able to run a Thunar plugin
which provides a property page.

%package shares
Group: Graphical desktop/Other
Summary: Opens the thunar-shares-plugin via the thunar-plugger wrapper
Requires: %name >= %version thunar-shares-plugin
BuildArch: noarch

%description shares
Opens the thunar-shares-plugin via the thunar-plugger wrapper.

%package dropbox
Group: Graphical desktop/Other
Summary: Opens the thunar-dropbox-plugin via the thunar-plugger wrapper
Requires: %name >= %version thunar-dropbox-plugin
BuildArch: noarch

%description dropbox
Opens the thunar-dropbox-plugin via the thunar-plugger wrapper.

%prep
%setup

%build
%xfce4reconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/thunar-plugger
%doc AUTHORS README

%files shares
%_desktopdir/thunar-plugger-shares.desktop

%files dropbox
%_desktopdir/thunar-plugger-dropbox.desktop

%changelog
* Fri Nov 25 2011 Paul Wolneykien <manowar@altlinux.ru> 1.3-alt1
- Try to adjust some "stocked" buttons to close the window on click.

* Thu Nov 10 2011 Paul Wolneykien <manowar@altlinux.ru> 1.2-alt1
- Use the base name as the file info name.

* Sat Sep 10 2011 Paul Wolneykien <manowar@altlinux.ru> 1.1-alt1
- Add a wrapper for the Dropbox plugin.

* Wed Sep 07 2011 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial version for ALT Linux based on shareman program.
