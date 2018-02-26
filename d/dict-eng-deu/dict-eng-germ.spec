%define dict_name_en eng-deu
%define dict_name_de deu-eng

Name: dict-%dict_name_en
Version: 0.2
Release: alt2.1.1

Summary: English-German Dictionary: dictd format
Summary(ru_RU.KOI8-R): Англо-немецкий словарь: формат dictd
License: GPL
Group: Text tools
PreReq: dictd
Url: http://www.freedict.org/ru/
Packager: Alexey Dyachenko <alexd@altlinux.ru>

Source: %dict_name_en.tar.gz
Source1: %dict_name_de.tar.gz

BuildArch: noarch

%description
Electronic version of English-German Dictionary, in dictd format.
You can use it with your favourite dict client.

%description -l ru_RU.KOI8-R
Электронная версия англо-немецкого словаря в формате dictd.
Вы можете использовать его со своим любимым dict клиентом.

%package -n dict-%dict_name_de
Summary: German-English Dictionary: dictd format
Summary(ru_RU.KOI8-R): Немецко-английский словарь: формат dictd
License: GPL
Group: Text tools
PreReq: dictd

%description -n dict-%dict_name_de
Electronic version of German-English Dictionary, in dictd format.
You can use it with your favourite dict client.

%description -n dict-%dict_name_de -l ru_RU.KOI8-R
Электронная версия немецкого-английского словаря в формате dictd.
Вы можете использовать его со своим любимым dict клиентом.

%prep
%setup -c -a1

%install
install -pD -m 644 %dict_name_en.dict.dz %buildroot%_datadir/dictd/%dict_name_en.dict.dz
install -pD -m 644 %dict_name_en.index %buildroot%_datadir/dictd/%dict_name_en.index
install -pD -m 644 %dict_name_de.dict.dz %buildroot%_datadir/dictd/%dict_name_de.dict.dz
install -pD -m 644 %dict_name_de.index %buildroot%_datadir/dictd/%dict_name_de.index

%post -n dict-%dict_name_en
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%postun -n dict-%dict_name_en
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%post -n dict-%dict_name_de
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%postun -n dict-%dict_name_de
%_sbindir/dictdconfig -w
%_initdir/dictd condreload

%files
%_datadir/dictd/%{dict_name_en}*

%files -n dict-%dict_name_de
%_datadir/dictd/%{dict_name_de}*

%changelog
* Thu Sep 27 2007 Slava Semushin <php-coder@altlinux.ru> 0.2-alt2.1.1
- NMU
- Fixed incomplete locale specification in Summary tag for
  dict-deu-eng package (finally fixed #11843)
- Removed unneeded dict-tools from BuildRequires

* Wed Jun 13 2007 Slava Semushin <php-coder@altlinux.ru> 0.2-alt2.1
- NMU
- Fixed incomplete locale specification in Summary tag (#11843)
- Set packager tag to previous maintainer
- Spec cleanup:
  + Updated Url tag
  + s/BuildArchitectures/BuildArch/
  + s/%%setup -q/%%setup/
  + s/$RPM_BUILD_ROOT/%%buildroot/
  + Replace some tabs to spaces
  + Remove one trailing space in %%description of dict-deu-eng package
  + Use %%_sbindir macros instead of appropriate path

* Thu Jan 30 2003 Alexey Dyachenko <alexd@altlinux.ru> 0.2-alt2
- fix bug #0001705:    1st installation doesn't check the new dictionary
	in at a running dictd
-	fix bug #0001700: preuninstall script turns dictd off
-	fix bug #0001701: preuninstall script turns dictd off
- fix install scripts

* Mon Oct 14 2002 Alexey Dyachenko <alexd@altlinux.ru> 0.2-alt1
- add missing PreReq: dictd

* Thu Sep 26 2002 Alexey Dyachenko <alexd@altlinux.ru> 0.1-alt1
- initial build for Alt Linux

