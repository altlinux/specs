# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-macros-fedora-compat
BuildRequires: /usr/bin/dot /usr/bin/gdlib-config /usr/bin/gpg /usr/bin/openssl perl(Class/Accessor.pm) perl(Class/Accessor/Fast.pm) perl(Digest/SHA.pm) perl(Exception/Class.pm) perl(Exception/Class/Base.pm) perl(GSSAPI.pm) perl(HTTP/Date.pm) perl(I18N/LangTags/Detect.pm) perl(LWP/Authen/Negotiate.pm) perl(LWP/MediaTypes.pm) perl(Net/LDAP.pm) perl(Net/LDAP/Constant.pm) perl(Net/LDAP/Control/Paged.pm) perl(Net/LDAP/Filter.pm) perl(Net/LDAP/Util.pm) perl(Params/Validate.pm) perl(Pod/Simple/HTMLBatch.pm) perl(Pod/Simple/Search.pm) perl(Pod/Simple/XHTML.pm) perl(Term/EditorEdit.pm) perl(URI.pm) perl(URI/QueryParam.pm) perl-podlators
# END SourceDeps(oneline)
# hacks around findreq ==============
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MRT::Base'
%add_findreq_skiplist %_sbindir/rt-externalize-attachments
%add_findreq_skiplist %_sbindir/rt-*
%add_findreq_skiplist */RT/ACL.pm
%add_findreq_skiplist */RT/Article.pm
%add_findreq_skiplist */RT/Authen/ExternalAuth.pm
%add_findreq_skiplist */RT/CustomField.pm
%add_findreq_skiplist */RT/Group.pm
%add_findreq_skiplist */RT/I18N*
%add_findreq_skiplist */RT/Queue.pm
%add_findreq_skiplist */RT/System.pm
%add_findreq_skiplist */RT/Ticket.pm
%add_findreq_skiplist */RT/Tickets.pm
%add_findreq_skiplist /usr/share/rt/upgrade/*
%add_findreq_skiplist /usr/libexec/perl5-tests/*
# end hacks =======================
BuildRequires: perl(Data/Perl/Role/Collection/Array.pm) perl(Encode/Guess.pm)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name rt
#
# Copyright (c) 2005-2017, Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# --with devel_mode/--without devel_mode
#	enable/disable building/installing devel files
#	Default: enabled
%bcond_without devel_mode

# --with runtests
#	run testsuite when building the rpm
#	Default: disabled (doesn't work in chroots.)
%bcond_with runtests

# --with mysql
#	configure for use with mysql
%bcond_with mysql
# --with pg
#	configure for use with postgress
%bcond_with pg

# default to mysql
%if !%{with mysql} && !%{with pg}
%global with_mysql 1
%endif

%global RT_BINDIR		%{_bindir}
%global RT_SBINDIR		%{_sbindir}
%global RT_FONTSDIR		%{_datadir}/%{name}/fonts
%global RT_LIBDIR		%{perl_vendor_privlib}
%global RT_WWWDIR		%{_datadir}/%{name}/html
%global RT_LEXDIR		%{_datadir}/%{name}/po
%global RT_LOGDIR		%{_localstatedir}/log/%{name}
%global RT_CACHEDIR		%{_localstatedir}/cache/%{name}
%global RT_LOCALSTATEDIR	%{_localstatedir}/lib/%{name}
%global RT_STATICDIR		%{_datadir}/%{name}/static

Name:		rt
Version:	4.4.1
Release:	alt1_3
Summary:	Request tracker

Group:		Networking/WWW
License:	GPLv2+
URL:		http://bestpractical.com/request-tracker
Source0:	http://download.bestpractical.com/pub/rt/release/rt-%{version}.tar.gz
# Notes on running the testsuite
Source1:	README.tests
# rt's Apache configuration
Source2:	rt.conf.in
# Fedora-specific installation notes
Source3:	README.fedora.in
# rt's logrotate configuration
Source4:	rt.logrotate.in

Patch1: 0001-Add-Fedora-configuration.patch
Patch2: 0002-Use-usr-bin-perl-instead-of-usr-bin-env-perl.patch
Patch3: 0003-Remove-fixperms-font-install.patch
Patch4: 0004-Fix-permissions.patch

BuildArch:	noarch

Obsoletes:	rt3 < %{version}-%{release}
Provides:	rt3 = %{version}-%{release}

# This list is alpha sorted
BuildRequires: rpm-build-perl
BuildRequires: perl(Apache/DBI.pm)
BuildRequires: perl(Apache/Session.pm)
BuildRequires: perl(Business/Hours.pm)
BuildRequires: perl(Cache/Simple/TimedExpiry.pm)
BuildRequires: perl(CGI/Cookie.pm)
BuildRequires: perl(CGI/PSGI.pm)
BuildRequires: perl(CGI/Emulate/PSGI.pm)
BuildRequires: perl(Class/ReturnValue.pm)
BuildRequires: perl(Convert/Color.pm)
BuildRequires: perl(CPAN.pm)
BuildRequires: perl(Crypt/Eksblowfish.pm)
BuildRequires: perl(Crypt/SSLeay.pm)
BuildRequires: perl(Crypt/X509.pm)
BuildRequires: perl(CSS/Minifier/XS.pm)
BuildRequires: perl(CSS/Squish.pm)
BuildRequires: perl(Data/GUID.pm)
BuildRequires: perl(Data/ICal.pm)
BuildRequires: perl(Data/Page/Pageset.pm)
BuildRequires: perl(Date/Extract.pm)
BuildRequires: perl(Date/Manip.pm)
BuildRequires: perl(DateTime/Format/Natural.pm)
BuildRequires: perl(Date/Format.pm)
BuildRequires: perl(DateTime.pm)
BuildRequires: perl(DateTime/Locale.pm)
%{?with_mysql:BuildRequires: perl(DBD/mysql.pm)}
%{?with_pg:BuildRequires: perl(DBD/Pg.pm)}
BuildRequires: perl(DBI.pm)
BuildRequires: perl(DBIx/SearchBuilder.pm)
BuildRequires: perl(Devel/StackTrace.pm)
BuildRequires: perl(Devel/GlobalDestruction.pm)
BuildRequires: perl(Digest/base.pm)
BuildRequires: perl(Digest/MD5.pm)
BuildRequires: perl(Email/Address.pm)
BuildRequires: perl(Email/Address/List.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(Errno.pm)
%{?with_devel_mode:BuildRequires: perl(File/Find.pm)}
BuildRequires: perl(File/Glob.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(File/Temp.pm)
BuildRequires: perl(File/Which.pm)
BuildRequires: perl(GD.pm)
BuildRequires: perl(GD/Graph.pm)
BuildRequires: perl(GD/Text.pm)
BuildRequires: perl(GnuPG/Interface.pm)
BuildRequires: perl(GraphViz.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(HTML/Entities.pm)
%{?with_devel_mode:BuildRequires: perl(HTML/Form.pm)}
BuildRequires: perl(HTML/FormatText.pm)
BuildRequires: perl(HTML/FormatText/WithLinks.pm)
BuildRequires: perl(HTML/FormatText/WithLinks/AndTables.pm)
BuildRequires: perl(HTML/Mason.pm)
BuildRequires: perl(HTML/Mason/PSGIHandler.pm)
BuildRequires: perl(HTML/Quoted.pm)
BuildRequires: perl(HTML/RewriteAttributes.pm)
BuildRequires: perl(HTML/Scrubber.pm)
BuildRequires: perl(HTML/TreeBuilder.pm)
BuildRequires: perl(HTTP/Request/Common.pm)
BuildRequires: perl(HTTP/Server/Simple.pm)
BuildRequires: perl(HTTP/Server/Simple/Mason.pm)
BuildRequires: perl(IPC/Run.pm)
BuildRequires: perl(IPC/Run3.pm)
BuildRequires: perl(IPC/Run/SafeHandles.pm)
BuildRequires: perl(JSON.pm)
BuildRequires: perl(JavaScript/Minifier.pm)
BuildRequires: perl(JavaScript/Minifier/XS.pm)
BuildRequires: perl(List/MoreUtils.pm)
BuildRequires: perl(Locale/Maketext.pm)
BuildRequires: perl(Locale/Maketext/Fuzzy.pm)
BuildRequires: perl(Locale/Maketext/Lexicon.pm)
BuildRequires: perl(Locale/PO.pm)
BuildRequires: perl(Log/Dispatch.pm)
BuildRequires: perl(Net/LDAP/Server/Test.pm)
%{?with_devel_mode:BuildRequires: perl(Log/Dispatch/Perl.pm)}
BuildRequires: perl(LWP.pm)
BuildRequires: perl(LWP/UserAgent.pm)
BuildRequires: perl(LWP/Protocol/https.pm)
BuildRequires: perl(Mail/Mailer.pm)
BuildRequires: perl(MIME/Entity.pm)
BuildRequires: perl(MIME/Types.pm)
%{?with_devel_mode:BuildRequires: perl(Module/Refresh.pm)}
BuildRequires: perl(Module/Versions/Report.pm)
BuildRequires: perl(Mozilla/CA.pm)
BuildRequires: perl(Mojo/DOM.pm)
BuildRequires: perl(Net/CIDR.pm)
BuildRequires: perl(Net/IP.pm)
BuildRequires: perl(Net/Server.pm)
BuildRequires: perl(Net/Server/PreFork.pm)
BuildRequires: perl(Net/SMTP.pm)
BuildRequires: perl(Net/SSL.pm)
BuildRequires: perl(PerlIO/eol.pm)
BuildRequires: perl(Pod/Usage.pm)
BuildRequires: perl(Pod/Select.pm)
BuildRequires: perl(Plack.pm)
BuildRequires: perl(Plack/Handler/Starlet.pm)
%{?with_devel_mode:BuildRequires: perl(Plack/Middleware/Test/StashWarnings.pm)}
BuildRequires: perl(Regexp/Common.pm)
BuildRequires: perl(Regexp/Common/net/CIDR.pm)
BuildRequires: perl(Regexp/IPv6.pm)
BuildRequires: perl(Role/Basic.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Scope/Upper.pm)
BuildRequires: perl(Set/Tiny.pm)
BuildRequires: perl(Storable.pm)
%{?with_devel_mode:BuildRequires: perl(String/ShellQuote.pm)}
BuildRequires: perl(Symbol/Global/Name.pm)
BuildRequires: perl(Term/ReadKey.pm)
BuildRequires: perl(Term/ReadLine.pm)
%{?with_devel_mode:BuildRequires: perl(Test/Builder.pm)}
%{?with_devel_mode:BuildRequires: perl(Test/Deep.pm)}
%{?with_devel_mode:BuildRequires: perl(Test/Email.pm)}
%{?with_devel_mode:BuildRequires: perl(Email/Abstract.pm)}
%{?with_devel_mode:BuildRequires: perl(Test/Expect.pm)}
%{?with_devel_mode:BuildRequires: perl(Test/MockTime.pm)}
%{?with_devel_mode:BuildRequires: perl(Test/NoWarnings.pm)}
%{?with_devel_mode:BuildRequires: perl(Test/Pod.pm)}
%{?with_devel_mode:BuildRequires: perl(Test/Warn.pm)}
%{?with_devel_mode:BuildRequires: perl(Test/WWW/Mechanize.pm)}
%{?with_devel_mode:BuildRequires: perl(Test/WWW/Mechanize/PSGI.pm)}
BuildRequires: perl(Text/ParseWords.pm)
BuildRequires: perl(Text/Password/Pronounceable.pm)
BuildRequires: perl(Text/Quoted.pm)
BuildRequires: perl(Text/Template.pm)
BuildRequires: perl(Text/WikiFormat.pm)
BuildRequires: perl(Text/Wrapper.pm)
BuildRequires: perl(Time/HiRes.pm)
BuildRequires: perl(Time/ParseDate.pm)
BuildRequires: perl(Tree/Simple.pm)
BuildRequires: perl(UNIVERSAL/require.pm)
%{?with_devel_mode:BuildRequires: perl(WWW/Mechanize.pm)}
BuildRequires: perl(XML/RSS.pm)
%{?with_devel_mode:BuildRequires: perl(XML/Simple.pm)}

%{?with_runtests:BuildRequires: perl(DBD/SQLite.pm)}
%{?with_runtests:BuildRequires: perl(Test/Warn.pm)}
%{?with_runtests:BuildRequires: perl(Test/MockTime.pm)}
%{?with_runtests:BuildRequires: perl(String/ShellQuote.pm)}
%{?with_runtests:BuildRequires: perl(Test/Expect.pm)}

BuildRequires:	/usr/bin/pod2man
BuildRequires:	/usr/sbin/apachectl

# the original sources carry bundled versions of these ...
Requires:  /usr/share/fonts/ttf/google-droid/DroidSansFallback.ttf
Requires:  /usr/share/fonts/ttf/google-droid/DroidSans.ttf
# ... we use symlinks to the system-wide versions ...
BuildRequires:	/usr/share/fonts/ttf/google-droid/DroidSansFallback.ttf
BuildRequires:	/usr/share/fonts/ttf/google-droid/DroidSans.ttf

Requires:	%{_sysconfdir}/httpd2/conf


# rpm doesn't catch these:
Requires: perl(Apache/Session.pm)
Requires: perl(Business/Hours.pm)
Requires: perl(Calendar/Simple.pm)
Requires: perl(CSS/Squish.pm)
Requires: perl(Data/Page.pm)
Requires: perl(Data/Page/Pageset.pm)
Requires: perl(Data/ICal.pm)
Requires: perl(Data/ICal/Entry/Event.pm)
%{?with_mysql:Requires: perl(DBD/mysql.pm) >= 2.101.800}
# This should be: Requires: perl(DBD::Pg) != 3.3.0
# cf. RHBZ#1138926
%{?with_pg:Requires: perl(DBD/Pg.pm)}
%{?with_pg:Conflicts: perl(DBD/Pg.pm) == 3.3.0}
Requires: perl(DateTime/Format/Natural.pm) >= 0.670
Requires: perl(Log/Dispatch/Perl.pm)
Requires: perl(GD/Text.pm)
Requires: perl(GD/Graph/bars.pm)
Requires: perl(GD/Graph/pie.pm)
Requires: perl(HTML/Quoted.pm)
Requires: perl(HTTP/Server/Simple/Mason.pm)
Requires: perl(HTML/Mason/Request.pm)
Requires: perl(I18N/LangTags/List.pm)
Requires: perl(IPC/Run3.pm)
Requires: perl(LWP/MediaTypes.pm)
Requires: perl(mod_perl2.pm)
Requires: perl(Module/Versions/Report.pm)
Requires: perl(Net/Server/PreFork.pm)
Requires: perl(PerlIO/eol.pm)
Requires: perl(Plack/Middleware/Test/StashWarnings.pm) >= 0.060
Requires: perl(Plack/Handler/Starlet.pm)
Requires: perl(Text/Quoted.pm)
Requires: perl(Text/WikiFormat.pm)
Requires: perl(Time/ParseDate.pm)
Requires: perl(URI/URL.pm)
Requires: perl(XML/RSS.pm)

# rpm fails to add these:
Provides: perl(RT/Shredder/Exceptions.pm)

# Split out. Technically, not actually necessary, but ... let's keep it for now.
Requires: rt-mailgate



# Keep FCGI optional

# Work-around rpm's depgenerator defect: 


# Filter redundant provides

# Filter bogus provides


Source44: import.info
%filter_from_requires /^perl\\(FCGI.ProcManager.pm\\)/d
%filter_from_requires /^perl\\(DBIx.SearchBuilder.Handle..pm\\)/d
%filter_from_provides /^perl\\(RT.pm\\)$/d
%filter_from_provides /^perl\\(HTML.Mason/d
%filter_from_provides /^perl\\(IO.Handle.CRLF.pm\\)$/d
Patch33: rt-4.4.1-alt-buildroot.patch
Conflicts: request-tracker < 4
#Obsoletes: request-tracker < 4
Provides: request-tracker = %version


%description
RT is an enterprise-grade ticketing system which enables a group of people
to intelligently and efficiently manage tasks, issues, and requests submitted
by a community of users.


%package mailgate
Summary: rt's mailgate utility
Group:	Networking/WWW
# rpm doesn't catch these:
Requires:	perl(Pod/Usage.pm)
Requires:	perl(HTML/TreeBuilder.pm)
Requires:	perl(HTML/FormatText.pm)
Obsoletes:	rt3-mailgate < %{version}-%{release}
Provides:	rt3-mailgate = %{version}-%{release}

%description mailgate
%{summary}


%if %{with devel_mode}
%package tests
Summary:	Test suite for package rt
Group:		Development/Debug
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/bin/prove
Requires:	perl(RT/Test.pm)
# rpm doesn't catch these:
Requires:	perl(DBD/SQLite.pm)
Requires:	perl(GnuPG/Interface.pm)
# Bug: The testsuite unconditionally depends upon perl(GraphViz)
Requires:	perl(GraphViz.pm)
Requires:	perl(Net/LDAP/Server/Test.pm)
Requires:	perl(Plack/Handler/Apache2.pm)
Requires:	perl(Set/Tiny.pm)
Requires:	perl(String/ShellQuote.pm)
Requires:	perl(Test/Deep.pm)
Requires:	perl(Test/Expect.pm)
Requires:	perl(Test/MockTime.pm)
Requires:	perl(Test/Warn.pm)

Obsoletes:	rt3-tests < %{version}-%{release}
Provides:	rt3-tests = %{version}-%{release}
Conflicts: request-tracker < 4

%description tests
%{summary}

# Running the tests leaves stray files
# remove everything by brute force.
%postun tests
if [ $1 -eq 0 ]; then
  %{__rm} -rf %{perl_testdir}/%{name}
fi


%package -n perl-RT-Test
Summary: rt's test utility module
Group:	Networking/WWW
Requires:	rt = %{version}-%{release}

# rpm doesn't catch these:
Requires:	perl(Test/WWW/Mechanize/PSGI.pm)
Requires:	perl(Mojo/DOM.pm)

%description -n perl-RT-Test
%{summary}

%endif # devel_mode

%prep
%setup -q -n rt-%{version}

sed -e 's,@RT_CACHEDIR@,%{RT_CACHEDIR},' %{SOURCE3} \
  > README.fedora
sed -e 's,@RT_LOGDIR@,%{RT_LOGDIR},' %{SOURCE4} \
  > rt.logrotate

# remove auto*generated files
find -name '*.in' | \
while read a; do b=$(echo "$a" | sed -e 's,\.in$,,'); rm "$b"; done

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# Propagate rpm's directories to config.layout
cat << \EOF >> config.layout

#   Fedora directory layout.
<Layout Fedora>
  bindir:		%{RT_BINDIR}
  sbindir:		%{RT_SBINDIR}
  sysconfdir:		%{_sysconfdir}/%{name}
  libdir:		%{RT_LIBDIR}
  manualdir:		%{_docdir}/%{name}/docs
  lexdir:		%{RT_LEXDIR}
  localstatedir:	%{RT_LOCALSTATEDIR}
  htmldir:		%{RT_WWWDIR}
  fontdir:		%{RT_FONTSDIR}
  staticdir:		%{RT_STATICDIR}
  logfiledir:		%{RT_LOGDIR}
  masonstatedir:	%{RT_CACHEDIR}/mason_data
  sessionstatedir:	%{RT_CACHEDIR}/session_data
  customdir:		%{_prefix}/local/lib/%{name}
  custometcdir:		%{_prefix}/local/etc/%{name}
  customhtmldir:	${customdir}/html
  customlexdir:		${customdir}/po
  customlibdir:		${customdir}/lib
</Layout>
EOF

# Comment out the Makefile trying to change groups/owners
# Fix DESTDIR support
sed -i \
	-e 's,	chgrp,	: chrgp,g' \
	-e 's,	chown,	: chown,g' \
	-e 's,$(DESTDIR)/,$(DESTDIR),g' \
	-e 's,-o $(BIN_OWNER) -g $(RTGROUP),,g' \
Makefile.in

# Install upgrade/ into %%{_datadir}/%%{name}/upgrade
sed -i -e 's,$(RT_ETC_PATH)/upgrade,%{_datadir}/%{name}/upgrade,g' Makefile.in
%patch33 -p1

%build
%configure \
--with-apachectl=/usr/sbin/apachectl \
--with-web-user=apache --with-web-group=apache \
--with-db-type=%{?with_mysql:mysql}%{?with_pg:Pg} \
--enable-layout=Fedora \
--with-web-handler=modperl2 \
--libdir=%{RT_LIBDIR}

make %{?_smp_mflags}

# Explicitly check for devel-mode deps
%{?with_devel_mode:%{__perl} ./sbin/rt-test-dependencies --verbose --with-%{?with_mysql:mysql}%{?with_pg:pg} --with-modperl2 --with-dev}

# Generate man-pages
for file in \
bin/rt \
bin/rt-crontool \
bin/rt-mailgate \
sbin/rt-attributes-viewer \
sbin/rt-clean-sessions \
sbin/rt-dump-metadata \
sbin/rt-email-dashboards \
sbin/rt-email-digest \
sbin/rt-email-group-admin \
sbin/rt-externalize-attachments \
sbin/rt-fulltext-indexer \
sbin/rt-importer \
sbin/rt-preferences-viewer \
sbin/rt-server \
sbin/rt-server.fcgi \
sbin/rt-session-viewer \
sbin/rt-setup-database \
sbin/rt-setup-fulltext-index \
sbin/rt-serializer \
sbin/rt-shredder \
sbin/rt-validate-aliases \
sbin/rt-validator \
sbin/standalone_httpd \
; do
/usr/bin/pod2man $file > $file.1
done


%install
make install DESTDIR=${RPM_BUILD_ROOT}

# Work-around to regression in rpm >= 4.12.90:
# Can't mix %%doc with directly installed docs, anymore.
# Need to install all files directly.
install -m 644 README README.fedora ${RPM_BUILD_ROOT}%{_docdir}/%{name}

# We don't want CPAN
rm -f ${RPM_BUILD_ROOT}%{_sbindir}/rt-test-dependencies

# Install apache configuration
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd2/conf
sed -e 's,@RT_WWWDIR@,%{RT_WWWDIR},g' \
  -e 's,@RT_SBINDIR@,%{RT_SBINDIR},g' \
  -e 's,@RT_BINDIR@,%{RT_BINDIR},g' \
  %{SOURCE2} > ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd2/conf/%{name}.conf

mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
for file in bin/*.1 sbin/*.1; do
install -m 0644 $file ${RPM_BUILD_ROOT}%{_mandir}/man1
done

# missed by "make install"
install -d -m755 ${RPM_BUILD_ROOT}%{RT_LOGDIR}
# missed by "make install"
install -d -m755 ${RPM_BUILD_ROOT}%{RT_LOCALSTATEDIR}

# install log rotation stuff
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d
install -m 644 rt.logrotate ${RPM_BUILD_ROOT}%{_sysconfdir}/logrotate.d/%{name}

# Symlink, %%{_sysconfdir}/%%{name}/upgrade is hard-coded at various places
ln -s %{_datadir}/%{name}/upgrade ${RPM_BUILD_ROOT}%{_sysconfdir}/%{name}/upgrade

install -d -m755 ${RPM_BUILD_ROOT}%{RT_FONTSDIR}
ln -s /usr/share/fonts/ttf/google-droid/DroidSans.ttf ${RPM_BUILD_ROOT}%{RT_FONTSDIR}
ln -s /usr/share/fonts/ttf/google-droid/DroidSansFallback.ttf ${RPM_BUILD_ROOT}%{RT_FONTSDIR}

install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}
cp -R t ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}

# Uninstalled stuff the testsuite accesses
install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/devel
cp -R devel/tools ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/devel
cp -R devel/docs ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/devel
# Some parts of the testsuite want relative paths
cp %{SOURCE1} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}
install -d -m755 ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share
ln -s %{RT_WWWDIR} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share/html
ln -s %{RT_STATICDIR} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/share/static
ln -s %{_bindir} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/bin
ln -s %{_sbindir} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/sbin
ln -s %{_sysconfdir}/%{name} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/etc
ln -s %{RT_LIBDIR} ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/lib
ln -s %{_docdir}/%{name}/docs ${RPM_BUILD_ROOT}%{perl_testdir}/%{name}/docs


# These files should not be installed
rm ${RPM_BUILD_ROOT}%{RT_LEXDIR}/*.pot
rm ${RPM_BUILD_ROOT}%{RT_LIBDIR}/RT/Generated.pm.in

# Fix permissions
find ${RPM_BUILD_ROOT}%{RT_WWWDIR} \
  -type f -exec chmod a-x {} \;

# Silence rpmlint
chmod a+x \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/3.8-ical-extension \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/4.0-customfield-checkbox-extension \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/generate-rtaddressregexp \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/sanity-check-stylesheets \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/shrink-cgm-table \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/shrink-transactions-table \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/switch-templates-to \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/time-worked-history \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/upgrade-articles \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/upgrade-mysql-schema.pl \
${RPM_BUILD_ROOT}%{_datadir}/%{name}/upgrade/vulnerable-passwords

%check
# The tests don't work in buildroots, they
# - require to be run as root
# - require an operational rt system
%{?with_runtests:make test}

%{!?with_runtests:/usr/bin/prove -l t/pod.t}

%postun
if [ $1 -eq 0 ]; then
  %{__rm} -rf %{RT_CACHEDIR}
fi


%files
%{_docdir}/%{name}
%doc COPYING
%{_bindir}/*
%{_sbindir}/*
%exclude %{_bindir}/rt-mailgate
%{_mandir}/man1/*
%exclude %{_mandir}/man1/rt-mailgate*
%{RT_LIBDIR}/*
%exclude %{RT_LIBDIR}/RT/Test*
%attr(0700,apache,apache) %{RT_LOGDIR}
%attr(0770,apache,apache) %{RT_LOCALSTATEDIR}

%dir %{_sysconfdir}/%{name}
%{_datadir}/%{name}/upgrade
%{_sysconfdir}/%{name}/upgrade
%{_sysconfdir}/%{name}/acl*
%{_sysconfdir}/%{name}/schema*
%{_sysconfdir}/%{name}/init*
%{?!with_pg:%exclude %{_sysconfdir}/%{name}/*.Pg}
%{?!with_pg:%exclude %{_datadir}/%{name}/upgrade/*/*.Pg}
%exclude %{_sysconfdir}/%{name}/*.Oracle
%exclude %{_datadir}/%{name}/upgrade/*/*.Oracle
%exclude %{_sysconfdir}/%{name}/*.SQLite
%exclude %{_datadir}/%{name}/upgrade/*/*.SQLite
%{?!with_mysql:%exclude %{_sysconfdir}/%{name}/*.mysql}
%{?!with_mysql:%exclude %{_datadir}/%{name}/upgrade/*/*.mysql}
%config(noreplace) %attr(0640,apache,apache) %{_sysconfdir}/%{name}/RT_*.pm
%dir %attr(770,apache,apache) %{_sysconfdir}/%{name}/RT_SiteConfig.d

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%dir %{_datadir}/%{name}
%{RT_WWWDIR}
%{RT_LEXDIR}
%{RT_FONTSDIR}
%{RT_STATICDIR}

%config(noreplace) %{_sysconfdir}/httpd2/conf/%{name}.conf

%dir %{RT_CACHEDIR}
%attr(0770,apache,apache) %{RT_CACHEDIR}/mason_data
%attr(0770,apache,apache) %{RT_CACHEDIR}/session_data

%files mailgate
%doc COPYING
%{_bindir}/rt-mailgate
%{_mandir}/man1/rt-mailgate*

%if %{with devel_mode}
%files tests
%dir %{perl_testdir}
%{perl_testdir}/%{name}
# Doesn't work outside of the source tree
%exclude %{perl_testdir}/%{name}/t/pod.t
# Required by t/shredder/*t
%{_sysconfdir}/%{name}/*.SQLite

%files -n perl-RT-Test
%doc COPYING
%dir %{RT_LIBDIR}/RT
%{RT_LIBDIR}/RT/Test*
%endif

%changelog
* Wed Feb 01 2017 Igor Vlasenko <viy@altlinux.ru> 4.4.1-alt1_3
- new version

