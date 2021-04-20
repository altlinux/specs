%define _unpackaged_files_terminate_build 1

Name: i3status
Version: 2.13
Release: alt1

Summary: I3 status bar generator for i3bar, dzen2, xmobar or similar programs.
License: BSD-like
Group: Graphical desktop/Other

URL: http://i3wm.org/i3status
Source: %name-%version.tar
# Patch adds "none" to the default config because
# current version of i3bar crashes without it
# Remove after corresponding correction of i3bar or 
# i3status.
#Patch1: %name-alt-config.patch

BuildRequires: libalsa-devel libconfuse-devel libyajl-devel
BuildRequires: libnl-devel libpulseaudio-devel
BuildRequires: asciidoc xmlto

%description
i3status is a small program (about 1500 SLOC) for generating a
status bar for i3bar, dzen2, xmobar or similar programs.
It is designed to be very efficient by issuing a very small number
of system calls, as one generally wants to update such a status line
every second. This ensures that even under high load, your status bar
is updated correctly. Also, it saves a bit of energy by not hogging
your CPU as much as spawning the corresponding amount of
shell commands would.

%description -l ru_RU.UTF-8
i3status это крошечная программа (размером примерно 1500 строк),
предназначенная для генерации строки статуса, используемой
программами i3bar, dzen2, xmobar и их аналогами.
При разработке i3status учитывалось то, что поскольку
строка статуса должна обновляться каждую секунду,
программа должна быть максимально эффективной и делать
минимальное кол-во системных вызовов. Поэтому, даже
при высокой нагрузке статусная строка будет корректно
обновляться. И, кроме того, это позволяет сберегать
электроэнергию, поскольку загрузка ЦП несопоставима
с загрузкой, вызванной соответствующим количеством
скриптов.

%prep
%setup -n %name-%version
#%%patch1 -p1

%build
%autoreconf
mkdir BUILD && pushd $_
ln -s ../configure
%configure --disable-sanitizers
%make_build
popd

%install
pushd BUILD
make DESTDIR=%buildroot install

# Добавляем нехитрую документацию.
%define docdir %_docdir/%name-%version

mkdir -p %buildroot/%docdir
popd

install -pm644 LICENSE %buildroot%docdir/
install -pm644 CHANGELOG %buildroot%docdir/

%files

%%doc %docdir
%config /etc/i3status.conf
%_bindir/*
%_man1dir/*

%changelog
* Tue Apr 20 2021 Slava Aseev <ptrnine@altlinux.org> 2.13-alt1
- Version update.

* Sat Mar 28 2015 Andrey Bergman <vkni@altlinux.org> 2.9-alt1
- Version update.

* Sun Jan 12 2014 Andrey Bergman <vkni@altlinux.org> 2.8-alt1
- Version update.

* Fri Apr 12 2013 Andrey Bergman <vkni@altlinux.org> 2.7-alt1
- Version update.

* Mon Oct 08 2012 Andrey Bergman <vkni@altlinux.org> 2.6-alt1
- Version update.

* Sat Aug 18 2012 Andrey Bergman <vkni@altlinux.org> 2.5.1-alt1
- Initial release for Sisyphus.

