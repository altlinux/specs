%define sourcename gkwebmon
%define plugin webmon

Name: gkrellm-%plugin
Version: 0.2
Release: alt2.1

Summary: GKrellM webmon plugin
Summary(ru_RU.CP1251): ѕлагин webmon дл€ GKrellM
License: GPL
Group: Monitoring
Url: http://%sourcename.sourceforge.net/
Source: http://prdownloads.sourceforge.net/%sourcename/%sourcename-%version.tgz

Patch0: gkwebmon-0.2-alt-i18n.patch.gz
Patch1: gkwebmon-0.2-alt-ru.patch.gz
Patch2: gkwebmon-0.2-alt-install.patch.gz

Provides: %sourcename = %version
Obsoletes: %sourcename <= %version

Requires: gkrellm >= 2.0

# Automatically added by buildreq on Tue Dec 02 2003
BuildRequires: gkrellm-devel glib2-devel libatk-devel libgtk+2-devel libpango-devel libssl-devel pkgconfig

%description
GKWebMon will monitor for changes in webpages by fetching webpages
and comparing MD5 with an initial MD5. When a monitored page changes
the plugin will give a warning by changing the apperance of an icon
decal. The pages that have changed will be shown in a tool tip. 

%description -l ru_RU.CP1251
GKWebMon следит за изменени€ми в в веб страницах скачива€ их и сравнива€
md5 суммы с предыдущими. ≈сли страница изменилась, изменитс€ цвет плагина
и отобразитс€ количество измененных страниц. јдреса измененных страниц
будут отображены в подсказке.

%prep
%setup -q -n %sourcename-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build enable_nls=1 LOCALEDIR=%_datadir/locale

%install
%__mkdir -p %buildroot%_libdir/gkrellm2/plugins
%make_install install enable_nls=1 PLUGIN_DIR=%buildroot%_libdir/gkrellm2/plugins INSTALL_PREFIX=%buildroot LOCALEDIR=%_datadir/locale
%find_lang %sourcename

%files -f %sourcename.lang
%doc ChangeLog
%_libdir/gkrellm2/plugins/*.so

%changelog
* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.2-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue May 18 2004 Alex Murygin <murygin@altlinux.ru> 0.2-alt2
- renamed to gkrellm-{NAME}
- added russian summary, description

* Tue Dec 02 2003 Alex Murygin <murygin@altlinux.ru> 0.2-alt1
- Built for ALTLinux

