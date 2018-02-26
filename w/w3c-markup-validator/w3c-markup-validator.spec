Name: w3c-markup-validator
Version: 1.2
Release: alt1
Summary: W3C Markup Validator helps check the validity of Web documents

Group: Networking/WWW
License: W3C Software License
Url: http://validator.w3.org/

Packager: Sergey Kurakin <kurakin@altlinux.org>

Source0: http://validator.w3.org/sgml-lib.tar
Source1: http://validator.w3.org/validator.tar

Source2: http://www.w3.org/Icons/WWW/w3c_home_nb.png
Source3: http://www.w3.org/QA/Tools/I_heart_validator.png
Source4: http://www.opensource.org/trademarks/opensource/web/opensource-55x48.jpg
Source5: %name.control
Source6: http://www.w3.org/Icons/WWW/w3c_home.png

Patch0: %name-1.2-alt-extsrc.patch
Patch1: %name-0.8.5-alt-warning.patch

BuildArch: noarch
BuildPreReq: rpm-macros-apache rpm-macros-apache2
BuildPreReq: perl-XML-LibXML sgml-common perl-Net-IP
Requires: %name-libs = %version-%release %name-config = %version-%release
Requires(pre): %name-control = %version-%release
Requires: perl(LWP/UserAgent.pm) >= 1.900 perl(Net/IP.pm)
Obsoletes: w3c-validator

# Automatically added by buildreq on Fri Sep 17 2010 (-bi)
BuildRequires: apache2-common control perl-CGI perl-Config-General perl-Encode-HanExtra perl-HTML-Encoding perl-HTML-Template perl-JSON perl-SGML-Parser-OpenSP

%description
Most Web documents are written using markup languages, such as HTML
or XHTML. These languages are defined by technical specifications, which
usually include a machine-readable formal grammar (and vocabulary).
The act of checking a document against these constraints is called
validation, and this is what the Markup Validator does.
This validator can process documents written in most markup languages.

Local installation of W3C Markup Validator is accessible by URL:
http://localhost/w3c-validator/

%package libs
Summary: SGML and XML DTDs for the W3C Markup Validator
Group: Networking/WWW
Requires: sgml-common
Obsoletes: w3c-validator-libs

%description libs
SGML and XML DTDs for the W3C Markup Validator.


%package control
Summary: Control facility for the W3C Markup Validator
Group: Networking/WWW
Requires: %name = %version-%release control

%description control
Control facility for the W3C Markup Validator
to easily switch Allow_Private_IPs mode


%package apache
Summary: Apache 1.3 config for W3C Markup Validator
Group: Networking/WWW
Requires: %name = %version-%release
Requires: apache
Provides: %name-config = %version

%description apache
Configuration files and scripts, required for W3C Markup Validator
to work with Apache 1.3.


%package apache2
Summary: Apache 2 config for W3C Markup Validator
Group: Networking/WWW
Requires: %name = %version-%release
Requires: apache2
Provides: %name-config = %version

%description apache2
Configuration files and scripts, required for W3C Markup Validator
to work with Apache 1.3.

%set_perl_req_method relaxed

%prep
%setup -q -a 1 -n validator-%version

mv htdocs/sgml-lib .
rm -rf htdocs
mv validator-%version/* .
rm -rf validator-%version

%patch0 -p2
%patch1 -p1

# localize configs.
sed -i 's|/usr/local/validator\b|%_datadir/%name|' \
	htdocs/config/validator.conf \
	httpd/conf/httpd.conf \
	httpd/cgi-bin/*
sed -i -r 's|^(\s*Library\s*=\s*).*|\1%_datadir/sgml/%name|' htdocs/config/validator.conf
sed -i 's|\bwww-validator\@w3\.org\b|root\@localhost|' htdocs/config/validator.conf
sed -i 's|/validator\.w3\.org/|/localhost/w3c-validator/|' htdocs/config/validator.conf

# prevent configuration error, if proxy module is not enabled
sed -i 's|<Proxy|<IfModule proxy>\n<Proxy|;s|</Proxy>|</Proxy>\n</IfModule>|' httpd/conf/httpd.conf

# make config for apache2
cp httpd/conf/httpd.conf httpd/conf/httpd2.conf
# make validator's dir accessible for apache2
echo '<IfModule authz_host_module>
<Directory /usr/share/w3c-markup-validator/>
	Order deny,allow
	Allow from all
</Directory>
</IfModule>' >> httpd/conf/httpd2.conf
# start site
echo 'w3c-markup-validator=yes' > httpd/conf/start_site.conf
# mod_cgi is required
echo 'cgi=yes' > httpd/conf/start_mods.conf

# move config out of the way
mv htdocs/config __config
sed -i "s|Templates = .*\$|Templates = %_datadir/%name/templates|g" __config/validator.conf
sed -i "s|#Base = |Base = |g" __config/validator.conf

# unfortunately, we need this two dummy files to prevent errors
# in case of new validator >=0.8.6 with old config <=0.8.5
# touch __config/eref.cfg __config/attref.cfg

%build

%install
# config files for validator
install -dm 755 %buildroot%_sysconfdir/w3c
install -pm 644 __config/* %buildroot%_sysconfdir/w3c
# config files for apache
install -Dpm 644 httpd/conf/httpd.conf %buildroot%apache_modconfdir/%name.conf
# config files for apache2
install -Dpm 644 httpd/conf/httpd2.conf %buildroot%apache2_extra_available/%name.conf
install -Dpm 644 httpd/conf/start_site.conf %buildroot%apache2_extra_start/10-%name.conf
install -Dpm 644 httpd/conf/start_mods.conf %buildroot%apache2_mods_start/10-%name.conf

# Scripts, HTML, etc.
install -dm 755 %buildroot%_datadir/%name
cp -pR httpd/cgi-bin htdocs share/templates %buildroot%_datadir/%name

# SGML library
install -dm 755 %buildroot%_datadir/sgml
cp -pR sgml-lib %buildroot%_datadir/sgml/%name
install -dm 755 %buildroot%_sysconfdir/sgml
touch %buildroot%_sysconfdir/sgml/%name-%version-%release.cat

# local copies of external images
install -pm 644 %SOURCE2 %buildroot%_datadir/%name/htdocs/images
install -pm 644 %SOURCE6 %buildroot%_datadir/%name/htdocs/images
install -pm 644 %SOURCE3 %buildroot%_datadir/%name/htdocs/images
install -pm 644 %SOURCE4 %buildroot%_datadir/%name/htdocs/images

# control facility
install -Dpm 755 %SOURCE5 %buildroot%_sysconfdir/control.d/facilities/%name

%pre
%pre_control %name

%post
%post_control -s restricted %name

%post apache
[ $1 -eq 1 ] && %post_apacheconf || :

%postun apache
%postun_apacheconf || :

%post apache2
%apache2_sbindir/a2chkconfig > /dev/null && %post_apache2conf || :

%postun apache2
[ $1 -eq 0 ] && %apache2_sbindir/a2chkconfig > /dev/null && %postun_apache2conf || :

%post libs
for catalog in sgml.soc xml.soc ; do
  install-catalog --add \
    %_sysconfdir/sgml/%name-%version-%release.cat \
    %_datadir/sgml/%name/$catalog >/dev/null 2>&1 || :
done

%preun libs
for catalog in sgml.soc xml.soc ; do
  install-catalog --remove \
    %_sysconfdir/sgml/%name-%version-%release.cat \
    %_datadir/sgml/%name/$catalog >/dev/null 2>&1 || :
done


%files
%config %_sysconfdir/w3c/
%_datadir/%name/

%files control
%_sysconfdir/control.d/facilities/%name

%files apache
%config %apache_modconfdir/%name.conf

%files apache2
%config %apache2_extra_available/*
%config %apache2_extra_start/*
%config %apache2_mods_start/*

%files libs
%ghost %config %_sysconfdir/sgml/%name-%version-%release.cat
%_datadir/sgml/%name/

%changelog
* Sat Sep 10 2011 Sergey Kurakin <kurakin@altlinux.org> 1.2-alt1
- 1.2

* Fri Sep 17 2010 Sergey Kurakin <kurakin@altlinux.org> 1.1-alt1
- 1.1
- more reliable config for apache2
- control facility to easily switch and remember Allow_Private_IPs mode

* Wed Jul 22 2009 Sergey Kurakin <kurakin@altlinux.org> 0.8.5-alt3
- unowned directory fixed

* Tue Jul 21 2009 Sergey Kurakin <kurakin@altlinux.org> 0.8.5-alt2
- added Requires: String/Approx.pm
- "This instance of the validator..." warning corrected
- fixed external sources in UI:
  + used local copies of images: w3c logo, Open Source logo etc.
  + removed w3c ads block

* Tue May  5 2009 Sergey Kurakin <kurakin@altlinux.org> 0.8.5-alt1
- 0.8.5:
  + new feature to suggest possible (valid) alternatives
  + some bug fixes, UI improvements, documentation updates

* Sat Jan 31 2009 Sergey Kurakin <kurakin@altlinux.org> 0.8.4-alt1
- 0.8.4, mostly bugfix release
- previously removed "user-agent" feature moved back (fixed in upstream)

* Mon Sep  8 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.8.3-alt2
- deactivated experimental "user-agent" feature
- spec cleanup (including post and postun scripts) with new macros
  from rpm-macros-apache and rpm-macros-apache2
- added BuildRequires; thus fixed most of Requires too
- added Requires, that can not be calculated by perlreq
  due to "set_perl_req_method relaxed"

* Thu Sep 04 2008 Gleb Stiblo <ulfr@altlinux.ru> 0.8.3-alt1
- new version
- include #15488 fix

* Fri Apr 25 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.8.2-alt1
- new version
- added support for apache2
- configuration files for apache and apache2 moved to different
  subpackages
- set_perl_req_method relaxed
- restored self-diagnostics in "check" script (paths to config
  files etc.)

* Wed Oct 04 2006 Gleb Stiblo <ulfR@altlinux.ru> 0.7.2-alt1
- new version
- package rename

* Fri Jun 11 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.6.1-alt5
- OpenSP added in requires

* Wed May 12 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.6.1-alt4
- spec cleanup
- checking for include line in httpd.conf added

* Mon May 03 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.6.1-alt3
- glibc 2.3 build

* Tue Apr 27 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.6.1-alt2
- post/postun scripts changed

* Tue Mar 23 2004 Gleb Stiblo <ulfr@altlinux.ru> 0.6.1-alt1
- ALT adaptation.
- -T removed from check

* Sun Dec  1 2002 Ville Skyttä <ville.skytta at iki.fi> - 0.6.1-1w3c
- Update to 0.6.1.

* Fri Nov 29 2002 Ville Skyttä <ville.skytta at iki.fi> - 0.6.0-1w3c
- First release.
