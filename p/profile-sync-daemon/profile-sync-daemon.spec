Name: profile-sync-daemon
Version: 6.21
Release: alt1
Summary: Offload browser profiles to RAM for speed a wear reduction
Summary(ru_RU.UTF-8): Выгружает профиль браузера в ОЗУ для ускорения его работы
License: MIT
Group: Networking/WWW
Url: https://github.com/graysky2/profile-sync-daemon
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Patch1: fix_distroname-alt.patch
BuildArch: noarch

%description
Profile-sync-daemon (psd) is a tiny pseudo-daemon designed to manage your
browser's profile in tmpfs and to periodically sync it back to your physical
disc (HDD/SSD). This is accomplished via a symlinking step and an innovative
use of rsync to maintain back-up and synchronization between the two. One of
the major design goals of psd is a completely transparent user experience.

To automatically start psd, use the command:
systemctl --user enable psd && systemctl --user start psd

%description -l ru_RU.UTF-8
Profile-sync-daemon (psd) представляет собой псевдо-демон, управляющий вашим
профилем браузера в tmpfs и периодически синхронизирующий его для восстановления
на вашем физическом диске (HDD/SSD). Это достигается с помощью создания
символических ссылок и инновационного использованию Rsync для резервного
копирования и синхронизации. Поддерживается большинство современных браузеров.

Для автоматического запуска psd, используйте команду:
systemctl --user enable psd && systemctl --user start psd

%prep
%setup
%patch1 -p2

%build
%make_build

%install
%makeinstall_std

%post
echo 'To automatically start psd, use the command:'
echo 'systemctl --user enable psd && systemctl --user start psd'

%files
%doc README*
%doc MIT
%_datadir/psd
%_bindir/*
%dir %_datadir/zsh
%dir %_datadir/zsh/site-functions/
%_datadir/zsh/site-functions/_psd
%_man1dir/*.1*
%_libexecdir/systemd/user/psd*.*

%changelog
* Sat May 14 2016 Anton Midyukov <antohami@altlinux.org> 6.21-alt1
- Initial build for ALT Linux Sisyphus
