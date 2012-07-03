Name: snowlist
Version: 1.0.2
Release: alt2

Summary: Mail and mailing lists to RSS gateway.
Group: Networking/Other
License: %gpl2only
Url: http://kiza.kcore.de/software/snowlist/
Packager: Mikhail Gusarov <dottedmag@altlinux.org>

# Automatically added by buildreq on Thu Nov 13 2008 (-bi)
BuildRequires: perl-DBI perl-Encode perl-MIME-tools perl-Text-Iconv perl-XML-LibXML

BuildPreReq: rpm-build-licenses rpm-build-perl perl-DBD-Pg

Source: %url/download/snowlist-1.0.2.tar.gz

%description
Snowlist is an application that processed incoming mails into an RDF (RSS 1.0)
feed that can be read by an RSS reader. The generated feed contains one item per
thread and groups all mails belonging to the same discussion into a bulletin
board like view. It is very useful to generate RSS feeds from mailing lists,
because it does not generate the usual one item per mail feeds that are next to
useless.

%prep
%setup

%build

%install

install -pD -m644 SnowlistConfig.pm %buildroot%perl_vendor_privlib/SnowlistConfig.pm
install -pD -m755 snowlistDB %buildroot%_bindir/snowlistDB
install -pD -m755 snowlistOutput %buildroot%_bindir/snowlistOutput
install -pD -m755 snowlistExpire %buildroot%_bindir/snowlistExpire

%files
%_bindir/snowlistDB
%_bindir/snowlistOutput
%_bindir/snowlistExpire
%perl_vendor_privlib/SnowlistConfig.pm
%doc Changelog
%doc README
%doc examples/config.example
%doc examples/createdb.postgres.sql
%doc examples/examplefeed.config

%changelog
* Fri Nov 14 2008 Mikhail Gusarov <dottedmag@altlinux.org> 1.0.2-alt2
- Added missing perl-DBD-Pg, perl-Encode dependencies
- Added patch for database name and host configuration
- Fixed problem with non-ASCII encodings

* Thu Nov 13 2008 Mikhail Gusarov <dottedmag@altlinux.org> 1.0.2-alt1
- First build for Sisyphus
