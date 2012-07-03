# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define php5_extension jpgraph

%define confextensiondir %_sysconfdir/php/%php5_extension
%define extensiondir %php5_moddir/%php5_extension
%define docdir %_docdir/%name-%version

Name: php5-%php5_extension
Version: 3.0.7
Release: %branch_release alt3

Summary: 2D graph plotting library for PHP
License: %qpl1
Group: System/Servers

Url: http://jpgraph.net
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

#see http://jpgraph.net/download/download.php?p=1
Source: %name-%version.tar
Source10: README.ALT-ru_RU.UTF-8
Source50: doc.apache.conf
Source60: doc.apache2.conf
Source61: doc.start.extra.conf
Source62: doc.start.mods.conf
Source70: examples.apache.conf
Source80: examples.apache2.conf
Source81: examples.start.extra.conf
Source82: examples.start.mods.conf
Patch: %name-%version-alt-config.patch

Provides: %extensiondir

Requires: php5 >= 5.2.0
Requires: php5-gd2
Requires: %docdir

BuildRequires(pre): rpm-build-php5
BuildRequires(pre): rpm-macros-branch
BuildRequires(pre): rpm-macros-apache
BuildRequires(pre): rpm-macros-apache2
BuildPreReq: rpm-build-licenses >= 2.0.4

%description
The JpGraph library is a 2D graph plotting library for PHP. It is meant
to significantly simplify the creation of dynamic graphs using PHP
scripting. The libray can be used on its own or as an embedded part of
a large WEB development undertaking. In addition the library allows
images to be created using the command line version of PHP
(the cli version).

%package examples
Summary: JpGraph examples
Group: System/Servers

Provides: %extensiondir/Examples

Requires: %name = %version-%release
Requires: %extensiondir
Requires: fonts-ttf-dejavu
Requires: fonts-ttf-vera
Requires: fonts-ttf-ms
#Requires: fonts-ttf-chinese-big5

%description examples
This package contains examples of using the JpGraph library.

%package examples-apache
Summary: Configuration of apache to display the JpGraph Example
Group: Networking/WWW

Requires: apache-base
Requires: %apache_modconfdir
Requires: %extensiondir/Examples

%description examples-apache
This package contains configuration files for the webserver apache,
for displaying JpGraph library Example.

%package examples-apache2
Summary: Configuration of apache2 (CGI) to display the JpGraph Example
Group: Networking/WWW

Requires: apache2-base
Requires: %apache2_extra_available
Requires: %apache2_extra_enabled
Requires: %apache2_extra_start
Requires: %apache2_mods_start
Requires: %extensiondir/Examples

%description examples-apache2
This package contains configuration files for the webserver apache2,
for displaying JpGraph library Example.

%package base-doc
Summary: JpGraph base documentation
Group: Books/Other
AutoReq: no

Provides: %docdir

%description base-doc
This package contains the JpGraph library base documentation.

%package doc
Summary: JpGraph documentation
Group: Books/Other
AutoReq: no

Provides: %docdir/html 

Requires: %docdir

%description doc
This package contains the JpGraph library documentation in HTML format.

%package doc-apache
Summary: Configuring of apache to display the html documentation JpGraph library
Group: Networking/WWW

Requires: apache-base
Requires: %apache_modconfdir
Requires: %docdir/html 

%description doc-apache
This package contains configuration files for the webserver apache,
for displaying HTML documentation JpGraph library.

%package doc-apache2
Summary: Configuring of apache2 to display the html documentation JpGraph library
Group: Networking/WWW

Requires: apache2-base
Requires: %apache2_extra_available
Requires: %apache2_extra_enabled
Requires: %apache2_extra_start
Requires: %apache2_mods_start
Requires: %docdir/html 

%description doc-apache2
This package contains configuration files for the webserver apache2,
for displaying HTML documentation JpGraph library.

%prep
%setup -n %name-%version
%patch0 -p1

%install
mkdir -p %buildroot%php5_moddir/
mkdir -p %buildroot%confextensiondir/
cp -a src %buildroot%extensiondir
mv %buildroot%extensiondir/jpg-config.inc.php \
	%buildroot%confextensiondir/
mv %buildroot%extensiondir/jpgraph_ttf.inc.php \
	%buildroot%confextensiondir/
ln -snf $(relative %buildroot%confextensiondir/jpg-config.inc.php \
	%buildroot%extensiondir/jpg-config.inc.php) \
	%buildroot%extensiondir/jpg-config.inc.php
ln -snf $(relative %buildroot%confextensiondir/jpgraph_ttf.inc.php \
	%buildroot%extensiondir/jpgraph_ttf.inc.php) \
	%buildroot%extensiondir/jpgraph_ttf.inc.php

mkdir -p %buildroot%docdir
install -m 644 README VERSION  %buildroot%docdir/
install -m 644 %SOURCE10 %buildroot%docdir/
cp -a docportal %buildroot%docdir/html/

# Install config for apache
install -m 644 -D %SOURCE50 %buildroot%apache_modconfdir/%name-doc.conf
install -m 644 -D %SOURCE70 %buildroot%apache_modconfdir/%name-examples.conf

# Install config for apache2
install -m 644 -D %SOURCE60 %buildroot%apache2_extra_available/%name-doc.conf
install -m 644 -D %SOURCE61 %buildroot%apache2_extra_start/100-%name-doc.conf
install -m 644 -D %SOURCE62 %buildroot%apache2_mods_start/100-%name-doc.conf
install -m 644 -D %SOURCE80 %buildroot%apache2_extra_available/%name-examples.conf
install -m 644 -D %SOURCE81 %buildroot%apache2_extra_start/100-%name-examples.conf
install -m 644 -D %SOURCE82 %buildroot%apache2_mods_start/100-%name-examples.conf

mkdir -p %buildroot%apache2_extra_enabled/
touch %buildroot%apache2_extra_enabled/%name-doc.conf
touch %buildroot%apache2_extra_enabled/%name-examples.conf

# Substitute the real paths in configs
find %buildroot%_sysconfdir -type f -print0 \
	| xargs -r0 sed -ri -e 's@%%docdir([-[:space:]/.,:}%%])@%docdir\1@g' \
		-e 's@%%php5_extension([-[:space:]/.,:}%%])@%php5_extension\1@g' \
		-e 's@%%extensiondir([-[:space:]/.,:}%%])@%extensiondir\1@g' \
		-e 's@%%name([-[:space:]/.,:}%%])@%name\1@g'

%post examples-apache
%post_apacheconf

%postun examples-apache
%postun_apacheconf

%post examples-apache2
%_sbindir/a2chkconfig >/dev/null
%post_apache2conf

%postun examples-apache2
%_sbindir/a2chkconfig >/dev/null
%postun_apache2conf

%post doc-apache
%post_apacheconf

%postun doc-apache
%postun_apacheconf

%post doc-apache2
%_sbindir/a2chkconfig >/dev/null
%post_apache2conf

%postun doc-apache2
%_sbindir/a2chkconfig >/dev/null
%postun_apache2conf

%files
%extensiondir/
%exclude %extensiondir/Examples
%config(noreplace) %confextensiondir/

%files examples
%extensiondir/Examples

%files examples-apache
%config(noreplace) %apache_modconfdir/%name-examples.conf

%files examples-apache2
%config(noreplace) %apache2_extra_available/%name-examples.conf
%ghost %apache2_extra_enabled/%name-examples.conf
%config(noreplace) %apache2_extra_start/100-%name-examples.conf
%config(noreplace) %apache2_mods_start/100-%name-examples.conf

%files base-doc
%doc %docdir/
%exclude %docdir/html/

%files doc
%doc %docdir/html/

%files doc-apache
%config(noreplace) %apache_modconfdir/%name-doc.conf

%files doc-apache2
%config(noreplace) %apache2_extra_available/%name-doc.conf
%ghost %apache2_extra_enabled/%name-doc.conf
%config(noreplace) %apache2_extra_start/100-%name-doc.conf
%config(noreplace) %apache2_mods_start/100-%name-doc.conf

%changelog
* Tue Apr 26 2011 Aleksey Avdeev <solo@altlinux.ru> 3.0.7-alt3
- Add provides %%_sysconfdir/php/jpgraph dir to %%name package

* Tue Apr 12 2011 Aleksey Avdeev <solo@altlinux.ru> 3.0.7-alt2
- Fix configuration files to apache{,2} in examples-apache{,2}
  subpackage

* Tue Apr 12 2011 Aleksey Avdeev <solo@altlinux.ru> 3.0.7-alt1
- Initial build for ALT Linux Sisyphus
