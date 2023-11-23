Name:    pipe-viewer
Version: 0.4.8
Release: alt1

Summary: A lightweight YouTube client for Linux, without requiring an API key.
License: Artistic-2.0
Group:   Other
Url:     https://github.com/trizen/pipe-viewer

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(Pre): rpm-build-perl
BuildRequires: perl-devel perl-Unicode-LineBreak perl-Gtk3 perl-Memoize perl-libwww perl-Module-Build perl-Data-Dump perl-LWP-Protocol-https perl-JSON perl-File-ShareDir libgtk+3-devel json ImageMagick-tools
Requires: perl-LWP-Protocol-https

%description
A lightweight application (fork of straw-viewer) for searching and playing videos from YouTube.

This fork parses the YouTube website directly and relies on the invidious instances only as a fallback method.

Package provides two versions of client:

- pipe-viewer - command-line interface to YouTube.
- gtk-pipe-viewer - GTK+ interface to YouTube.

%prep
%setup

%build
%perl_vendor_build --gtk3

%install
%perl_vendor_install

# replacing desktop stuff in right plases
mkdir -p %buildroot%_desktopdir
mv %buildroot%perl_vendor_privlib/auto/share/dist/WWW-PipeViewer/gtk-pipe-viewer.desktop %buildroot%_desktopdir/

# install menu icons
for N in 16 32 48 64 128;
do
convert share/icons/gtk-pipe-viewer.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/gtk-pipe-viewer.png
done

%files
%doc *.md
%_bindir/%name
%_bindir/gtk-pipe-viewer
%dir	%perl_vendor_privlib/WWW/PipeViewer
	%perl_vendor_privlib/WWW/PipeViewer.pm
	%perl_vendor_privlib/WWW/PipeViewer/*.pm
%dir	%perl_vendor_privlib/auto/share/dist/WWW-PipeViewer/icons
%dir	%perl_vendor_privlib/auto/share/dist/WWW-PipeViewer
	%perl_vendor_privlib/auto/share/dist/WWW-PipeViewer/icons/*.png
	%perl_vendor_privlib/auto/share/dist/WWW-PipeViewer/icons/*.jpg
	%perl_vendor_privlib/auto/share/dist/WWW-PipeViewer/icons/*.gif
	%perl_vendor_privlib/auto/share/dist/WWW-PipeViewer/gtk-pipe-viewer.glade
%_iconsdir/hicolor/*/apps/gtk-pipe-viewer.png
%_desktopdir/gtk-pipe-viewer.desktop
%_man1dir/%name.1.xz

%changelog
* Thu Nov 23 2023 Artyom Bystrov <arbars@altlinux.org> 0.4.8-alt1
- Initial build for Sisyphus