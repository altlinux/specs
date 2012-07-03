Name: gitolite
Version: 3.03
Release: alt1

Summary: Highly flexible server for git directory version tracker
License: %gpl2only
Group: System/Servers

Url: http://github.com/sitaramc/gitolite
Source0: %name-%version.tar
# actually fedora's too but the naming would be confusing;
# it does fit nicely though
Source1: README.ALT
Source2: gitolite.logrotate
# (fedora) Far from being upstreamable
Patch: gitolite-3.0-rpm.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 20 2011 (-bi)
# optimized out: perl-Encode perl-Text-Balanced
BuildRequires(pre): rpm-build-licenses
BuildRequires: perl-Text-Markdown

%define gitolite_homedir %_localstatedir/%name

%description
Gitolite allows a server to host many git repositories and
provide access to many developers, without having to give them
real userids on the server.  The essential magic in doing this
is ssh's pubkey access and the authorized keys file, and the
inspiration was an older program called gitosis.

Gitolite can restrict who can read from (clone/fetch) or write
to (push) a repository. It can also restrict who can push to what
branch or tag, which is very important in a corporate environment.
Gitolite can be installed without requiring root permissions, and
with no additional software than git itself and perl. It also has
several other neat features described below and elsewhere in the
doc/ directory.

%prep
%setup
%patch
cp %SOURCE1 .

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING

%build
# Format documentation
for F in doc/*.mkd; do
        perl -MText::Markdown >${F/.mkd/.html} <$F \
                -e 'print Text::Markdown::markdown (join "", <>)'
done

%install
install -d %buildroot%gitolite_homedir/.ssh
install -d %buildroot%_bindir
install -d %buildroot%perl_vendor_privlib
install -d %buildroot%_datadir/%name
install -d %buildroot%_logdir/%name

install -p src/gitolite %buildroot%_bindir
install -p src/gitolite-shell %buildroot%_bindir
cp -a src/lib/* %buildroot%perl_vendor_privlib
cp -a src/{VREF,commands,syntactic-sugar,triggers} %buildroot%_datadir/%name
cp -a check-g2-compat convert-gitosis-conf %buildroot%_datadir/%name

touch %buildroot%gitolite_homedir/.ssh/authorized_keys

# VERSION file
echo "v%version-%release" > %buildroot%_datadir/%name/VERSION

install -d %buildroot%_logrotatedir
install -m 640 %SOURCE2 %buildroot%_logrotatedir/%name

%pre
# FIXME: _%name?
getent group %name >/dev/null || groupadd -r %name ||:
getent passwd %name >/dev/null || \
useradd -r -g %name -d %gitolite_homedir -s /bin/sh \
        -c "git repository hosting" %name ||:

%triggerpostun  -- gitolite < 3.0
echo "---------------- gitolite -------------------------"
echo "  WARNING: there are no automatic upgrade procedure"
echo "  from gitolite g2 (2.x) to the g3 (3.x)"
echo "  See instructions for manual migration in"
echo "  g2migr*.html files in doc directory."
echo "---------------------------------------------------"

%files
%doc doc/*.html *README*
%doc --no-dereference COPYING

%_bindir/*
%perl_vendor_privlib/*
%_datadir/%name

%attr(750,%name,%name) %dir %gitolite_homedir
%attr(750,%name,%name) %dir %gitolite_homedir/.ssh
%config(noreplace) %attr(640,%name,%name) %gitolite_homedir/.ssh/authorized_keys

%attr(0730,root,%name) %dir %_logdir/%name

%config %_logrotatedir/%name

%changelog
* Wed Jun 13 2012 Nikolay A. Fetisov <naf@altlinux.ru> 3.03-alt1
- new version (Closes: #27442)

* Wed Apr 20 2011 Michael Shigorin <mike@altlinux.org> 2.0-alt1
- initial build for ALT Linux Sisyphus
  + based on 2.0-1 fedora package by Jon Ciesla <limb/jcomserv.net>
