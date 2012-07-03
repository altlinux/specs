%add_findprov_lib_path %_libdir/purple-2

%define pidgin_ver 2.0.0

Summary:	Purple-based antispam bot for Pidgin
Name:		purple-plugin-bot-sentry
Version:	1.1.0

Release:	alt3.qa1
License:	GPL
Group:		Networking/Instant messaging
Url:		http://sourceforge.net/projects/pidgin-bs/
Source:		%name-%version.tar

Requires:      libpurple >= %pidgin_ver
BuildRequires: libgtk+2-devel libtalkfilters-devel libxmms-devel  perl-XML-Parser
BuildRequires: pidgin-devel >= %pidgin_ver

%description
Bot Sentry is a Pidgin (libpurple) plugin to prevent Instant Message (IM) spam. It allows you to ignore IMs unless the sender is in your Buddy List, the sender is in your Allow List, or the sender correctly answers a question you have predefined. This release also contains Russian translations by Yury A. Romanov.

%prep
%setup -q -n %name-%version

%build
%configure --libdir=%_libdir/purple-2
%make_build

%install
%make_install DESTDIR=%buildroot install
%find_lang plugin_pack


%files 
%doc AUTHORS ChangeLog COPYING README
%_datadir/locale/*/LC_MESSAGES/bot-sentry.mo
%_libdir/purple-2

%changelog
* Wed Sep 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.0-alt3.qa1
- NMU (by repocop): the following fixes applied:
  * deprecated-packages-info-i18n-common for purple-plugin-bot-sentry
  * postclean-05-filetriggers for spec file

* Sat Nov 24 2007 Yury A. Romanov <damned@altlinux.ru> 1.1.0-alt3
- Added "Ignore you are added" messages feature (this requires a special patch to pidgin)

* Sat Nov 24 2007 Yury A. Romanov <damned@altlinux.ru> 1.1.0-alt2
- Fixes in Russian translations
- Cleaned source code
- Authorization requests deny successfully. 

* Sat Nov 24 2007 Yury A. Romanov <damned@altlinux.ru> 1.1.0-alt1
- Added some hooks to block authorization requests.
- Fixed in Russian translations. 

* Fri Nov 23 2007 Yury A. Romanov (damned) <damned@altlinux.ru> 1.1.0-alt0
- Initial build.
- Added Russian localization. 

