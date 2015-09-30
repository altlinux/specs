%define theme_name TheBear

Name: openbox-theme-%theme_name
Version: 3.3
Release: alt1.rc2

Summary: A Openbox theme engine - %theme_name
Summary(ru_RU.UTF-8): Тема для Openbox - %theme_name
License: %gpl2plus
Group: Graphical desktop/Other
Url: http://openbox.org/

BuildArch: noarch

# http://git.openbox.org/?p=mikachu/openbox.git;a=tree;f=themes/TheBear;hb=refs/tags/openbox-3_0-rc2-RELEASE
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

Conflicts: openbox-base <= 3.5.0-alt5

%description
This package contains the Openbox theme engine named TheBear.
This theme removed from the kit Openbox between versions 3.3-rc2 and 3.3.0.

%description -l ru_RU.UTF-8
Этот пакет содержит тему TheBear для Openbox.
Данная тема была удалена из Openbox между версиями 3.3-rc2 и 3.3.0.

%install
install -d %buildroot%_datadir/themes/%theme_name
(cd %buildroot%_datadir/themes/%theme_name && tar xvf %SOURCE0)

%files
%_datadir/themes/%theme_name

%changelog
* Fri Sep 11 2015 Aleksey Avdeev <solo@altlinux.org> 3.3-alt1.rc2
- Initial release for ALT Linux Sisyphus.
