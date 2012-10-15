%define installdir %webserver_webappsdir/%name
%define otrs_user otrs

Name: otrs
Version: 3.1.10
Release: alt1

Summary: Open source Ticket Request System
Group: Networking/WWW
License: AGPLv3
Url: http://www.otrs.org/

Packager: Pavel Zilke <zidex at altlinux dot org>

BuildArch: noarch

Requires(pre): %{_sbindir}/useradd
Requires(post): perl
Requires: webserver-common perl-CGI perl-DBI perl-DBD-mysql perl-Crypt-PasswdMD5 perl-Net-DNS perl-ldap perl-GD perl-GD-Text perl-GD-Graph perl-PDF-API2 perl-Compress-Zlib perl-Unicode-Normalize
BuildRequires(pre): rpm-macros-webserver-common rpm-macros-apache2 >= 3.9
BuildRequires: perl-CGI perl-DBI perl-DBD-mysql perl-Crypt-PasswdMD5 perl-Net-DNS perl-ldap perl-GD perl-GD-Text perl-GD-Graph perl-PDF-API2 perl-Compress-Zlib

Source0: %name-%version.tar.gz
Source1: apache2.conf
Source2: README.ALT
Patch: patch0.patch

%add_findreq_skiplist */bin/*
%add_findreq_skiplist */Kernel/*
%add_findreq_skiplist */scripts/*

%description
OTRS is an Open source Ticket Request System (also well known as trouble ticket system)
with many features to manage customer telephone calls and e-mails.
The system is built to allow your support, sales, pre-sales, billing,
internal IT, helpdesk, etc. department to react quickly to inbound inquiries.

%package apache2
Summary: Apache 2.x web-server configuration for %name
Group: Networking/WWW
Requires: %name = %version-%release, apache2, apache2-mod_perl perl-Apache-DBI
%description apache2
Apache 2.x web-server configuration for %name

%package doc-admin-en-pdf
Summary: %name admin manual (En)
Group: Networking/WWW
%description doc-admin-en-pdf
%name admin manual (En)

%package doc-admin-de-pdf
Summary: %name admin manual (De)
Group: Networking/WWW
%description doc-admin-de-pdf
%name admin manual (De)

%prep
%setup
%patch -p0

%install
# install apache config
install -pD -m0644 %_sourcedir/apache2.conf %buildroot%_sysconfdir/httpd2/conf/addon.d/A.%name.conf
# install otrs
mkdir -p %buildroot%installdir
cp -rp * %buildroot%installdir/
#install docs
install -pD -m0644 %_sourcedir/README.ALT README.ALT
mv %buildroot%installdir/doc/OTRSDatabaseDiagram.mwb OTRSDatabaseDiagram.mwb
mv %buildroot%installdir/doc/OTRSDatabaseDiagram.png OTRSDatabaseDiagram.png
mv %buildroot%installdir/doc/manual/en/otrs_admin_book.pdf admin_en.pdf
mv %buildroot%installdir/doc/manual/de/otrs_admin_book.pdf admin_de.pdf
#replace '/opt/otrs' to '/var/www/webapps/otrs' in all files
find %buildroot%installdir -type f -exec sed -i -e "s/\/opt\/otrs/\/var\/www\/webapps\/otrs/g" {} \;
# remove files
find %buildroot%installdir -name *.spec -delete
find %buildroot%installdir -name *.conf -delete
#install default config
cp %buildroot%installdir/Kernel/Config.pm.dist %buildroot%installdir/Kernel/Config.pm
cd %buildroot%installdir/Kernel/Config/
for foo in *.dist; do cp $foo `basename $foo .dist`; done
cd %buildroot%installdir/var/cron/
for foo in *.dist; do cp $foo `basename $foo .dist`; done

# all needed files packaged from %%builddir
rm -f %buildroot%installdir/ARCHIVE
rm -f %buildroot%installdir/CHANGES
rm -f %buildroot%installdir/COPYING-Third-Party
rm -f %buildroot%installdir/CREDITS
rm -f %buildroot%installdir/Custom/README
rm -f %buildroot%installdir/INSTALL
rm -f %buildroot%installdir/INSTALL.RedHat
rm -f %buildroot%installdir/INSTALL.SuSE
rm -f %buildroot%installdir/README
rm -f %buildroot%installdir/README.database
rm -f %buildroot%installdir/README.webserver
rm -f %buildroot%installdir/UPGRADING

%pre
if id %otrs_user >/dev/null 2>&1; then
    # update groups
    usermod -g %webserver_group %otrs_user
    # update home dir
    usermod -d %installdir %otrs_user
else
   %_sbindir/useradd -r  -g %webserver_group -c 'OTRS User' -d %installdir -s '/dev/null' %otrs_user >/dev/null 2>&1 ||:
fi

%post
cd %installdir/bin/
./otrs.SetPermissions.pl --otrs-user=%otrs_user --web-user=root --otrs-group=%webserver_group --web-group=%webserver_group %installdir >/dev/null 2>&1
#./Cron.sh start %otrs_user >/dev/null 2>&1

%postun
rm -rf %_docdir/%name-%version/

%post apache2
%post_apache2_rpma2chkconfigfile

%postun apache2
%post_apache2_rpma2chkconfigfile

%files
%doc COPYING
%doc RELEASE
%doc CHANGES
%doc COPYING-Third-Party
%doc OTRSDatabaseDiagram.mwb
%doc OTRSDatabaseDiagram.png
%doc README.ALT
%doc README
%doc Custom/README
%defattr(0775,root, %webserver_group)
%dir %installdir
%config(noreplace) %attr(0660,root,%webserver_group) %installdir/Kernel/Config.pm
%config(noreplace) %attr(0660,root,%webserver_group) %installdir/Kernel/Config/GenericAgent.pm
%installdir/bin
%installdir/Kernel
%installdir/scripts
%installdir/doc
%installdir/var
%installdir/COPYING
%installdir/RELEASE

%files apache2
%config(noreplace) %attr(0644,root,root) %_sysconfdir/httpd2/conf/addon.d/A.%name.conf

%files doc-admin-en-pdf
%doc admin_en.pdf

%files doc-admin-de-pdf
%doc admin_de.pdf

%changelog
* Tue Oct 09 2012 Sergey Y. Afonin <asy@altlinux.ru> 3.1.10-alt1
- New version
   Warning: OTRS 3.1 supports only UTF-8 as internal character set.
            Non-UTF-8 installations of OTRS must switch to UTF-8.
- added perl-Unicode-Normalize to Requires
- described GenericAgent.pm as %%config
- used %%post_apache2_rpma2chkconfigfile instead of "httpd2 condreload"

* Tue Feb 07 2012 Pavel Zilke <zidex at altlinux dot org> 2.4.11-alt1.2
- spec fixes

* Fri Sep 30 2011 Pavel Zilke <zidex at altlinux dot org> 2.4.11-alt1.1
- spec fixes

* Thu Sep 29 2011 Pavel Zilke <zidex at altlinux dot org> 2.4.11-alt1
- Security fixes:
  + Vulnerabilities in OTRS-Core allows read access to any file on local file system;
    CVE-2011-2746 (ALT #26186)

* Mon Oct 25 2010 Pavel Zilke <zidex at altlinux dot org> 2.4.9-alt1
- Security fixes:
  + AgentTicketZoom is vulnerable to XSS attacks from HTML e-mails;
    OSA-2010-03 (ALT #24419)

* Wed Sep 22 2010 Pavel Zilke <zidex at altlinux dot org> 2.4.8-alt1
- New version 2.4.8

* Sun Feb 21 2010 Pavel Zilke <zidex at altlinux dot org> 2.4.7-alt1
- Security fixes:
  + Vulnerability in OTRS-Core allows SQL-Injection;
    CVE-2010-0438 (ALT #22947)

* Thu Jan 21 2010 Pavel Zilke <zidex at altlinux dot org> 2.4.6-alt1
- Initial build for ALT Linux

