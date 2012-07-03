%define theme eyes

Name: xboard-theme-%theme
Version: 0.1
Release: alt1

URL: http://linuz.sns.it/~monge/wiki/index.php/Chess_pieces

Summary: xboard theme '%theme' from Maurizio Monge
License: LGPL
Group: Graphics

Packager: Stanislav Ievlev <inger@altlinux.org>

Source: %name-%version.tar

BuildRequires: ImageMagick

Requires: xboard
Provides: xboard-theme

%description
xboard theme '%theme' from Maurizio Monge  <maurizio.monge@gmail.com>

%prep
%setup -q
for s in 58 54 49 45 40 37 33 ;do
    for i in *64.xpm;do convert -resize ${s}x${s} $i ${i%%64*}${s}.xpm;done
done

%install
%__install -d %buildroot%_datadir/xboard/theme
cp -a *.xpm %buildroot%_datadir/xboard/theme

%files
%_datadir/xboard/theme

%changelog
* Thu Oct 18 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
