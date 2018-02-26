Name: fortune-mod-ru
Version: 1.33
Release: alt1

Summary: Russian fortune messages

Group: Games/Other
License: GPL
Url: http://acid-jack.tk

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: %name-%version.tar.bz2

# Automatically added by buildreq on Mon Jun 20 2005 (-bb)
BuildRequires: fortune-mod

%description
Russian fortune messages from Acid Jack

%package -n fortunes-ru
Summary: Russian fortune messages
Group: Games/Other
Requires: fortune-mod

%description -n fortunes-ru
Russian fortune messages from Acid Jack

%package -n fortunes-vekshin
Summary: Russian fortune messages
Group: Games/Other
Requires: fortune-mod

%description -n fortunes-vekshin
Russian fortune messages from Acid Jack.
Collected by Vekshin.

%prep
%setup -q

%install
%__mkdir_p %buildroot%_gamesdatadir/fortune

#(cd vekshin && mv adv adv.old && tr -d "[\r]" <adv.old >adv && rm adv.old)
find ./ -name *.dat | xargs rm -f
for ir in ru vekshin; do
	cd $ir
	for i in `ls -1`; do
		iconv -f koi8-r -t utf8 --replace='?' <${i} \
			>%buildroot%_gamesdatadir/fortune/$ir-${i}
		strfile %buildroot%_gamesdatadir/fortune/$ir-${i}
	done
	cd -
done

%files -n fortunes-ru
%doc ChangeLog README
%_gamesdatadir/fortune/ru*

%files -n fortunes-vekshin
%doc ChangeLog README
%_gamesdatadir/fortune/vekshin*

%changelog
* Thu Jul 28 2005 Vitaly Lipatov <lav@altlinux.ru> 1.33-alt1
- new version (fixed bug # 7453)
- add Url

* Mon Jun 20 2005 Vitaly Lipatov <lav@altlinux.ru> 1.32-alt0.1
- first build for ALT Linux Sisyphus
