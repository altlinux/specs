Name: rss2mail2
Version: 2.29
Release: alt2

Summary: An RSS aggregator that delivers feeds as plain text email
License: GPL or Artistic
Group: Networking/News
URL: http://exo.org.uk/code/rss2mail/
BuildArch: noarch
Source: rss2mail2

# this dependency cannot be detected automatically
Requires: perl-Class-DBI-SQLite

# Automatically added by buildreq on Mon Nov 15 2010 (-bi)
BuildRequires: perl-AppConfig perl-Class-DBI-BaseDSN perl-Class-DBI-SQLite perl-Exception-Class perl-HTML-FormatText-WithLinks perl-MIME-Lite perl-MIME-tools perl-Pod-Parser perl-Text-Autoformat perl-Text-Diff perl-XML-Feed

%description
rss2mail2 is an RSS aggregator for those that like to get all their
information delivered to their inbox. It runs through your list of feeds
and sends you one mail per updated feed containing all the new and
updated items in that feed. Optionally it will provide you with a
universal style diff of the updated feeds.

%prep
%setup -cT
cp -pv %SOURCE0 %name

%build
pod2man --release='%name v%version' %name %name.1
cat >%{name}rc <<'__EOF__'
base_dir	= ${HOME}/.%name
dsn		= dbi:SQLite:dbname=${HOME}/.%name/rss.db
mail_from	= %name
mail_to		= ${USER}
mail_per_item	= 1
oldest		= 120
max_not_found	= 32
__EOF__

%install
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 %name.1 %buildroot%_man1dir/%name.1
install -pD -m644 %{name}rc %buildroot/etc/%{name}rc

# for perl.req
%define __spec_autodep_custom_pre export HOME=%buildroot
cp -pv %buildroot/etc/%{name}rc %buildroot/.%{name}rc

%files
%_bindir/%name
%_man1dir/%name.1*
%config(noreplace) /etc/%{name}rc

%changelog
* Mon Nov 15 2010 Dmitry V. Levin <ldv@altlinux.org> 2.29-alt2
- Fixed build with new perl.

* Thu Feb 01 2007 Alexey Tourbin <at@altlinux.ru> 2.29-alt1
- 2.27 -> 2.29
- imported into git and adapted for gear
- changed author/date formatting, added category
- fixed multiline titles
- added sample procmail recipe

* Wed Aug 02 2006 Alexey Tourbin <at@altlinux.ru> 2.27-alt2
- send mail in reverse order
- increase max_not_found

* Thu Apr 20 2006 Alexey Tourbin <at@altlinux.ru> 2.27-alt1
- 2.26 -> 2.27
- all patches merged upstream

* Sun Sep 25 2005 Alexey Tourbin <at@altlinux.ru> 2.26-alt1
- 2.25 -> 2.26; clean_rss-pubDate.patch merged upstream

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 2.25-alt1
- initial revision:
  + alt-pod.patch: fixed layout for manpage
  + encode-subject.patch: use encode_mimeword() for subject
  + clean_rss-pubDate.patch: fixed a bug in substitution
