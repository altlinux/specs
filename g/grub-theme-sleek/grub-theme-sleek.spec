%define grub_normal white/dark-gray
%define grub_high black/white

Name: grub-theme-sleek
Version: 1.0
Release: alt1

Summary: GRUB bootloader themes for Simply Linux
License: GPLv2+
Group: System/Base
URL: https://github.com/sandesh236/sleek--themes

BuildArch: noarch

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source2: simply.png
Source3: alt.png

%description
%summary

%define themes bigsur dark white orange simply
%{expand:%(\
    for theme in %{themes}; do \
        echo -e "%%package -n grub-theme-$theme";\
        echo -e "Summary: $theme theme for GRUB\nGroup: Graphical desktop/Other\n";\
        echo -e "%%description -n grub-theme-$theme\n$theme theme for GRUB in 1366x768 resolution mode.\n";\
        echo -e "%%files -n grub-theme-$theme\n%ifarch %ix86 x86_64\n%_datadir/gfxboot/$theme\n\/boot/splash/$theme\n%endif\n/boot/grub/themes/$theme\n";\
    done\
)}

%prep
%setup

mv "Sleek theme-bigSur" sleek-theme-bigsur 
mv "Sleek theme-dark" sleek-theme-dark 
mv "Sleektheme-orange" sleek-theme-orange 
mv "Sleek theme-white" sleek-theme-white 
mv "Sleek theme-simply" sleek-theme-simply

for theme in bigsur dark white orange simply;do
	cp %SOURCE2 sleek-theme-$theme/sleek/icons/simply.png;
	cp %SOURCE3 sleek-theme-$theme/sleek/icons/slinux.png
done

mv "sleek-theme-bigsur/sleek" sleek-theme-bigsur/bigsur 
mv "sleek-theme-dark/sleek" sleek-theme-dark/dark 
mv "sleek-theme-orange/sleek" sleek-theme-orange/orange 
mv "sleek-theme-white/sleek" sleek-theme-white/white
mv "sleek-theme-simply/sleek" sleek-theme-simply/simply


%install
%ifarch %ix86 x86_64
for theme in bigsur dark white orange simply;do
mkdir -p %buildroot/boot/splash/;
cp -dpr --no-preserve=ownership  sleek-theme-$theme/$theme %buildroot/boot/splash/
done
%endif
for theme in bigsur dark white orange simply;do
mkdir -p %buildroot/boot/grub/themes/;
cp -dpr --no-preserve=ownership  sleek-theme-$theme/$theme %buildroot/boot/grub/themes/
done

%post
[ "$1" -eq 1 ] || exit 0
%ifarch %ix86 x86_64
ln -snf $theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/$theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message
%endif
. shell-config
shell_config_set /etc/sysconfig/grub2 GRUB_THEME /boot/grub/themes/$theme/theme.txt
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_NORMAL %grub_normal
shell_config_set /etc/sysconfig/grub2 GRUB_COLOR_HIGHLIGHT %grub_high

%postun
for theme in bigsur dark white orange simply;do
cp -an /etc/default/grub.bak /etc/default/grub
done

%changelog
* Mon Mar 27 2023 Artyom Bystrov <arbars@altlinux.org> 1.0-alt1
- initial build for ALT Sisyphus
