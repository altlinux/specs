Name: url_handler
Version: 0.3.1
Release: alt1

Group: Networking/Other
Summary: Opens URLs of common types with dedicated programs
Summary(ru_RU.UTF-8): Открывает URL-ы обычных типов предназначенными для них программами
License: GPLv2+
BuildArch: noarch

# There was a single pkg before: it used to unite urlview & url_handler.
Conflicts: urlview < 0:0.9-ipl8mdk

# url_handler.sh uses tr:
Requires: coreutils

# Probably something like this should be present, but not now.
#Requires: webclient
# Now very few pkgs provide webclient.

# We use 'mailx' command not present in older mailx
Conflicts: mailx < 0:8.1.2-alt1

# 2 scripts of our own.
Source: url_handler-%version.tar

%define confdir %_sysconfdir/urlview

%description
url_handler can be used as a uniform centralized handler for URLs of
common types by other programs (e.g., urlview) or human users.
It has a configurable list of programs dedicated to handling each specific
URL type: it is initialized to the list of the most popular programs.

Examples:

\#1
url_handler.sh http://lrn.ru \# open it in a browser

\#2
url_handler.sh ./manual.html \# view the local file from the working dir

%description -l ru_RU.UTF-8
url_handler может быть использован другими программами (например,
urlview) или людьми-пользователями для единообразной централизованной
обработки URL-ов обычных типов.  Имеется настраиваемый список программ,
предназначенных для обработки каждого отдельного типа URL: изначально
установлен список, перечисляющий самый популярные программы.

Примеры:

\#1
url_handler.sh http://lrn.ru \# открыть сайт в браузере

\#2
url_handler.sh ./manual.html \# посмотреть локальный файл из рабочей директории

%prep
%setup

%install
mkdir -p "%buildroot"{%_bindir,%confdir}
install -pm755 url_handler.sh "%buildroot"%_bindir/
ln -s ../..%_bindir/url_handler.sh "%buildroot"%confdir/url_handler.sh
install -pm644 url_handlers "%buildroot"%confdir/

%files
%_bindir/*
%dir %confdir/
%confdir/url_handler.sh
%config(noreplace) %confdir/url_handlers

%changelog
* Wed Nov 24 2010 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- url_handler.sh: added "mailto" type autodetection (closes: #24627).
- url_handlers: changed mailx mode to XT (closes: #17538).
- url_handler.sh: treat BROWSER and MAILER environment variables as
  colon-separated lists without necessary full path (closes: #3482).

* Fri Feb 08 2008 Dmitry V. Levin <ldv@altlinux.org> 0.3.0-alt2
- Added serial number to "conflicts" tags.

* Sun Mar 11 2007 Dmitry V. Levin <ldv@altlinux.org> 0.3.0-alt1
- Made %_bindir/url_handler.sh a regular file.
- Made %confdir/url_handler.sh a relative symlink to %_bindir/url_handler.sh.
- Removed symlink to license.
- url_handlers:
  + Fixed path to xvt (#10694).
  + Added http_prgs to ftp_prgs.
  + Added konqueror to https_prgs (#4798).
  + Added kmail to mailto_prgs (#4798).
  + Added w3m to https_prgs.
  + Removed netscape from https_prgs.
- url_handler.sh:
  + Implemented heuristics to recognize local paths (#6062).
  + Fixed error handling of unknown URL and missing handler.
  + Added URL type sanitation.
  + Implemented $BROWSER and $MAILER environment variables support (#3482).
  + Implemented printf(1) format symbols support in handler commands.

* Sun Jan 09 2005 Alexey Gladkov <legion@altlinux.ru> 0.2.1-alt2
- add more url-handlers (firefox, thunderbird).

* Thu Sep 18 2003 Ivan Zakharyaschev <imz@altlinux.ru> 0.2.1-alt1
- split pkg: urlview + url_handler (the old changelog is below):
  + the config-files remain under /etc/urlview/;
- expand ./* file paths to absolute (No. 1098);
- tiny changes: Error() function & other;
- translate Summary & description into Russian.

* Thu Sep 18 2003 Ivan Zakharyaschev <imz@altlinux.ru> 0.2.1-alt0
- Extractions from the old changelog of urlview (concerning url_handler):

@ Sat Feb  8 2003 Ivan Zakharyaschev <imz@altlinux.ru> 0.9-ipl7mdk
- url_handler.sh:
  + more quotes (to prevent expansion in wrong places; fixes No. 0001108);
  + accept ./@ as file-URL, too (fixes No. 0001098 at http://bugs.altlinux.ru);
- spec-file:
  + drop PreReq on sh-utils, use bash parameter expansion to get the basename.

@ Mon Apr 15 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.9-ipl5mdk
- url_handlers: added "file" method (by default, equals to http).
- url_handler.sh: added "file" protocol recognition (#0000838).

@ Thu Apr 11 2002 Ivan Zakharyaschev <imz@altlinux.ru> 0.9-ipl4mdk
- url_handler.sh:
  + clean up (ldv, imz);
  + extract the program lists to %_sysconfdir/urlview/url_handlers;
  + include user's configuration from ~/.etc/urlview/url_handlers;
  + case-insensitive protocol matching (fixes \#824 at bugs.altlinux.ru);
- url_handlers:
  + add mozilla -compose for mailto (fixes \#510 at bugs.altlinux.ru);
- spec-file:
  + maintaining patches is difficult, so use our own source for url_handler.sh;

@ Thu Nov 29 2001 Ivan Zakharyaschev <imz@altlinux.ru> 0.9-ipl3mdk
- a special directory %_sysconfdir/%name/ to hold both the conf-file and
  the script to start browsers (since it should be editable by the
  administrator -- it contains paths and preferences) (debian)
- add nohup-mode to start programs in X (debian)
- add more url-handlers:
  + gecko-based HTTP-browsers;
  + Sylpheed & mailto program (Mutt remains the first);
  + gFTP client;
- make the url-handler script more flexible (path lists implemented
  with Bash arrays)

@ Fri Nov 10 2000 Dmitry V. Levin <ldv@fandra.org> 0.9-ipl2mdk
- Fixed paths for browsers.
