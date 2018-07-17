Name:					netemul
Version:				1.0
Release:				alt1
Summary:				Is a program for simulating computer networks.
Summary(ru_RU.UTF-8):	Программа для визуализации работы компьютерных сетей.
License:				GPLv2
Group:					Education
Url:					http://netemul.sourceforge.net/
Packager:				Ivan Razzhivin <underwit@altlinux.org>
Source:					%name-%version.tar
Patch0:					netemul-1.0-alt-fix-gcc-4.5.patch
Patch1:					netemul-1.0-alt-fix-project-file.patch

BuildRequires: 			gcc-c++ libqt4-devel rpm-macros-qt4

%description
Program NetEmul has been created for visualisation operations of
computer networks, for simplification of understanding processes
occurring in network. Except training, the program opens ample
opportunities for experiments.

%description -l ru_RU.UTF-8
Программа NetEmul была создана для визуализации работы компьютерных
сетей, для облегчения понимания происходящих в ней процессов. Кроме
обучения, программа открывает широкие возможности для экспериментов и
их наглядного отображения.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i.bak 's!/usr/local/!/usr/!' ./netemul.desktop

%build
PATH=$PATH:%_qt4dir/bin/
%qmake_qt4 "PREFIX=%_prefix"
%make_build

%install
%make_install INSTALL_ROOT=%buildroot install

%files
%doc copyright GPL-2
%_bindir/netemul
%_desktopdir/netemul.desktop
%_datadir/netemul/*

%changelog
* Tue Jul 17 2018 Ivan Razzhivin <underwit@altlinux.org> 1.0-alt1
- Build for ALT
