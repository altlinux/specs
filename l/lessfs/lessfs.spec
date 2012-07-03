Summary: Lessfs is an inline data deduplicating filesystem
Name: lessfs
Version: 1.5.12
Release: alt1
License: GPLv3+
Group: System/Base
Url: http://www.lessfs.com
Source: http://downloads.sourceforge.net/%name/%name-%version.tar.gz

BuildRequires: libtokyocabinet-devel libdb4.8-devel libssl-devel libmhash-devel libfuse-devel liblzo2-devel

%description
Lessfs is an inline data deduplicating filesystem.

%prep
%setup
subst "s|/data/mta|%_localstatedir/%name/mta|g" etc/lessfs.cfg-bdb
subst "s|/data|%_localstatedir/%name|g" etc/lessfs.cfg-bdb
subst "s|ENCRYPT_DATA=on|ENCRYPT_DATA=off|g" etc/lessfs.cfg-bdb

%build
%autoreconf
%configure --with-crypto --with-berkeleydb --with-lzo
%make_build

%install
%makeinstall_std
install -D -m 644 etc/lessfs.cfg-bdb %buildroot/etc/lessfs.cfg

mkdir -p %buildroot/%_localstatedir/%name/{dta,mta}

rm -rf %buildroot%_datadir/%name
rm -rf %buildroot%_libdir/lib%name.a

%__cat << EOF > README.ALT
Система готова для работы из коробки.
Предполагается что данные и метаданные располагаются в соответствующих директориях в %_localstatedir/%name
Возможно для увеличения производительности Вы захотите чтобы они располагались на разных дисках. В таком случае их расположение нужно исправить в /etc/lessfs.cfg
Шифрование данных и метаданных по умолчанию отключено, но возможно использовать. В таком случае при монтировании будет задаваться пароль.

Для первого запуска и в случае изменения диреторий расположения данных и метаданных нужно запустить:
# mklessfs -f -c /etc/lessfs.cfg

После этого можно монтировать вручную:
# lessfs /etc/lessfs.cfg /mnt/lessfs

Или прописав в /etc/fstab строчку:
lessfs#/etc/lessfs.cfg  /mnt/lessfs     fuse    noauto  0       0

EOF

%files
%doc FAQ ChangeLog COPYING README README.ALT
%_bindir/*
%_sbindir/*
%_man1dir/*
%config(noreplace) /etc/lessfs.cfg
%dir %_localstatedir/%name
%dir %_localstatedir/%name/dta
%dir %_localstatedir/%name/mta

%changelog
* Mon Jun 11 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.5.12-alt1
- Build for ALT

