%define _unpackaged_files_terminate_build 1

Name: ydotool
Version: 1.0.4
Release: alt1

Summary: Generic command-line automation tool (no X!)
License: AGPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/ReimuNotMoe/ydotool

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-systemd
BuildRequires: cmake
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(scdoc)

%description
ydotool is not limited to Wayland. You can use it on anything as long as
it accepts keyboard/mouse/whatever input. For example, X11, text console,
"RetroArch OS", fbdev apps (fbterm/mplayer/SDL1/LittleVGL/Qt Embedded),
etc.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

# create special udev-rule
mkdir -p %buildroot%_udevrulesdir/
cat <<EOF > %buildroot%_udevrulesdir/80-uinput.rules
## ydotoold fix
##     https://github.com/ReimuNotMoe/ydotool/issues/25#issuecomment-535842993
KERNEL=="uinput", GROUP="input", MODE="0660", OPTIONS+="static_node=uinput"
EOF

%post
echo "NOTE: you have to start and enable ydotool daemon"
echo "      for current user using command:"
echo "            systemctl enable --now --user ydotool.service"
echo "      and then add your user to the 'input' group by"
echo "            su -l -c \"usermod -a -G input \$USER\""
echo "      Finally reboot the machine to activate the installed udev rule."

%files
%doc LICENSE README.md
%_bindir/*
%_man1dir/*
%_man8dir/*
%_userunitdir/*.service
%_udevrulesdir/80-uinput.rules

%changelog
* Sat May 24 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
