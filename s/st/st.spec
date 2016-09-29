Name: st
Version: 0.7
Release: alt1
Summary: A simple terminal implementation for X
License: MIT
Group: Terminals
Url: http://st.suckless.org/

# repacked http://dl.suckless.org/st/%name-%version.tar.gz
Source0: %name-%version.tar

Source1: st.desktop
Source2: st-user
Source3: st-user.1

Requires: fonts-ttf-liberation
Requires: alternatives

# Automatically added by buildreq on Fri Sep 16 2016
# optimized out: fontconfig fontconfig-devel libX11-devel libXrender-devel libfreetype-devel pkg-config python-base xorg-kbproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libXft-devel

%description
A simple virtual terminal emulator for X which sucks less.

%package user
Summary: Sources and tools for user configuration of st
Group: Terminals
License: MIT
Requires: %name = %EVR

%description user
Source files for st and a launcher/builder wrapper script for
customized configurations.

%prep
%setup
sed -i.backup -e 's|-Os|%optflags|' config.mk
cmp -s config.mk{,.backup} && false

sed -i.backup -e "s!^\(LDFLAGS.*$\)!\1 %{?__global_ldflags}!" config.mk
cmp -s config.mk{,.backup} && false

# terminfo entries are provided by ncurses-base
sed -i.backup -e "/@tic/d" Makefile
cmp -s Makefile{,.backup} && false

%build
%make_build

%install
%makeinstall_std PREFIX=%prefix
mv %buildroot%_bindir/st{,.bin}
install -pm755 %SOURCE2 %buildroot%_bindir/st-user
install -Dpm644 %SOURCE3 %buildroot%_mandir/man1/st-user.1

sed -i -e 's/VERSION/%version/' \
       -e 's/RELEASE/%release/' \
       %buildroot%_bindir/st-user \
       %buildroot%_mandir/man1/st-user.1

mkdir -p %buildroot%_datadir/applications/
cp %SOURCE1 %buildroot%_datadir/applications/st.desktop

mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%name <<EOF
%_bindir/st	%_bindir/st.bin	10
/usr/bin/xvt	%_bindir/st	10
EOF

cat >%buildroot%_altdir/%name-user <<EOF
%_bindir/st	%_bindir/st-user	20
EOF

%files
%_altdir/%name
%_bindir/st.bin
%_man1dir/st.1*
%_datadir/applications/st.desktop
%doc LICENSE FAQ LEGACY README TODO st.info

%files user
%_altdir/%name-user
%_bindir/st-user
%_man1dir/st-user.1*

%changelog
* Mon Sep 19 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7-alt1
- Initial build.
