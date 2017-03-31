Name: installer-feature-sudo-enable-by-default
Version: 1.0
Release: alt1

Summary: Setup sudo for users in wheel groop by default
Summary(ru_RU.UTF8): Настройка утилиты sudo для пользователей входящих в группу wheel
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Source: %name-%version.tar
BuildArch: noarch

%description
Setup sudo for users in wheel groop by default

%description -l ru_RU.UTF8
Настройка утилиты sudo для пользователей входящих в группу wheel
для работы по умолчанию. Утилита настоена как в Ubuntu,
т.е пользователь может выполнять любые административные задачи,
введя свой пароль.

%package stage3
Summary: Setup sudo for users in wheel groop by default
Summary(ru_RU.UTF8): Настройка утилиты sudo для пользователей входящих в группу wheel
License: GPL
Group: System/Configuration/Other

Requires: sudo

%description stage3
Setup sudo for users in wheel groop by default

%description stage3 -l ru_RU.UTF8
Настройка утилиты sudo для пользователей входящих в группу wheel
для работы по умолчанию. Утилита настоена как в Ubuntu,
т.е пользователь может выполнять любые административные задачи,
введя свой пароль.

%prep
%setup -q

%install
%makeinstall

%files stage3
%_datadir/install2/postinstall.d/*

%changelog
* Wed Mar 22 2017 Mikhail Efremov <sem@altlinux.org> 1.0-alt1
- Make it stage3 feature instead of stage2.
- Don't replace sudoers from package.

* Thu Aug 04 2011 Mikhail Efremov <sem@altlinux.org> 0.1-alt2
- Drop installer-stage2 requires.
- Drop Packager.
- Remove trailing spaces in description.

* Thu Jun 04 2009 Denis Koryavov <dkoryavov@altlinux.org> 0.1-alt1
- Initial build


