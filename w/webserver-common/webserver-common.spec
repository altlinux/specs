# vim: set ft=spec: -*- rpm-spec -*-
# hey Emacs, its -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

Name: webserver-common
Version: 1.4
Release: %branch_release alt1

Summary: Common resources for the Web srvers
Summary(ru_RU.KOI8-R): Общие ресурсы для Web серверов 
License: %asl
Group: System/Servers

Url: http://httpd.apache.org
Packager: Aleksey Avdeev <solo@altlinux.ru>
BuildArch: noarch

Source1: altlinux.png
# rpm macro definitions
Source2: webserver-rpm-macros.spec.inc
Source3: webserver-uploadsdir.control

# include webserver-rpm-macros.spec.inc
%include %SOURCE2

PreReq: %name-control >= 1.4

Provides: %webserver_datadir
Provides: %webserver_htdocsdir
Provides: %webserver_htdocsaddondir
Provides: %webserver_manualaddonsdir
Provides: %webserver_cgibindir
Provides: %webserver_iconsdir
Provides: %webserver_iconssmalldir
Provides: %webserver_vhostdir
Provides: %webserver_webappsdir
Provides: %webserver_uploadsdir

Conflicts: apache-common < 1.3.41rusPL30.23-alt4.1
Conflicts: apache-cgi-bin < 1.3.41rusPL30.23-alt4.1
Conflicts: apache-html < 1.3.41rusPL30.23-alt4.1
Conflicts: apache-icons < 1.3.41rusPL30.23-alt4.1
Conflicts: apache2-cgi-bin < 2.2.8-alt2.1
Conflicts: apache2-html < 2.2.9-alt5
Conflicts: apache2-icons < 2.2.8-alt2.1
Conflicts: apache2-manual-addons < 2.2.9-alt5
Conflicts: vhosts-filesystem < 0.2-alt1.2

BuildRequires(pre): rpm-macros-branch
BuildPreReq: rpm-build-licenses
BuildPreReq: control

%description
The package is the resources necessary for Web servers.

%description -l ru_RU.KOI8-R
В этом пакете находятся ресурсы, необходимые для Web серверов.


%package control
Summary: Control scripts for the Web srvers common resources
Summary(ru_RU.KOI8-R): Скрипты control для ресурсов Web серверов 
Group: System/Servers

PreReq: %_controldir

%description control
The package is the control scripts for Web servers common resources.

%description control -l ru_RU.KOI8-R
В этом пакете находятся скрипты control для ресурсов Web серверов.


%package -n rpm-macros-%name
Summary: RPM macros to rebuild Web servers and apps packages
Summary(ru_RU.KOI8-R): RPM макросы для сборки пакетов веб-серверов и приложений
Group: Development/Other

Conflicts: %name < 1.0

%description -n rpm-macros-%name
The package provide a set of macros for packaging Web applications
according to the ALT Linux Web Packaging Policy.

%description -n rpm-macros-%name -l ru_RU.KOI8-R
Макросы для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.


%package -n rpm-build-%name
Summary: RPM helper to rebuild Web servers and apps packages
Summary(ru_RU.KOI8-R): Набор утилит для автоматической Web серверов и приложений
Group: Development/Other

Conflicts: %name < 1.0
Requires: rpm-macros-%name >= %version

%description -n rpm-build-%name
These helper provide possibility to rebuild Web servers and applications
packages by some ALT Linux Web Packaging Policy.

%description -n rpm-build-%name -l ru_RU.KOI8-R
Набор утилит для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.


%prep
%setup -cTn %name-%version

%build
sed -e 's/^%%define[[:space:]]\+/%%/' %SOURCE2 > webserver.rpm-macros
sed -e 's|@webserver_uploadsdir@|%webserver_uploadsdir|g' \
	-e 's|@webserver_group@|%webserver_group|g' \
	-e 's|@webserver_webmaster@|%webserver_webmaster|g' \
	%SOURCE3 > webserver-uploadsdir.control

%install

install -d -m755 %buildroot%webserver_htdocsdir/
install -d -m755 %buildroot%webserver_htdocsaddondir/
install -d -m755 %buildroot%webserver_manualaddonsdir/
install -d -m755 %buildroot%webserver_cgibindir/
install -d -m755 %buildroot%webserver_iconsdir/
install -d -m755 %buildroot%webserver_iconssmalldir/
install -d -m755 %buildroot%webserver_vhostdir/
install -d -m755 %buildroot%webserver_webappsdir/
install -d -m755 %buildroot%webserver_uploadsdir/

install -pD -m644 %SOURCE1 %buildroot%webserver_iconsdir/

install -pD -m644 webserver.rpm-macros \
	%buildroot%_rpmmacrosdir/%name

install -pD -m755 webserver-uploadsdir.control \
	%buildroot%_controldir/webserver-uploadsdir

mkdir -p %buildroot%_rpmlibdir
cat <<\EOF >%buildroot%_rpmlibdir/%name-files.req.list
# %name dirlist for %_rpmlibdir/files.req
%webserver_datadir/	%name
%webserver_htdocsdir/	%name
%webserver_htdocsaddondir/	%name
%webserver_manualaddonsdir/	%name
%webserver_cgibindir/	%name
%webserver_iconsdir/	%name
%webserver_iconssmalldir/	%name
%webserver_vhostdir/	%name
%webserver_webappsdir/	%name
%webserver_uploadsdir/	%name
EOF

# SCRIPTS

%pre
%_sbindir/groupadd -r -f %webserver_group 2>/dev/null ||:
%_sbindir/groupadd -r -f %webserver_webmaster 2>/dev/null ||:
%pre_control webserver-uploadsdir

%post
%post_control -s webmasteronly webserver-uploadsdir

%files control
%_controldir/webserver-uploadsdir

%files -n rpm-macros-%name
%_rpmmacrosdir/%name

%files -n rpm-build-%name
%_rpmlibdir/%name-files.req.list

%files
%attr(-,root,%webserver_webmaster) %dir %webserver_datadir/
%attr(2775,root,%webserver_webmaster) %dir %webserver_htdocsdir/
%attr(2771,root,%webserver_webmaster) %dir %webserver_htdocsaddondir/
%attr(2771,root,%webserver_webmaster) %dir %webserver_cgibindir/
%attr(2775,root,%webserver_webmaster) %dir %webserver_iconsdir/
%attr(2775,root,%webserver_webmaster) %dir %webserver_iconssmalldir/
%attr(2771,root,%webserver_webmaster) %dir %webserver_vhostdir/
%attr(2771,root,%webserver_webmaster) %dir %webserver_webappsdir/
%attr(2755,root,root) %dir %webserver_uploadsdir/
%defattr(644,root,%webserver_webmaster,2775)
%webserver_iconsdir/altlinux.png

%changelog
* Tue Oct 12 2010 Aleksey Avdeev <solo@altlinux.ru> 1.4-alt1
- Add %%webserver_uploadsdir dir
- Add build %%name-control subpackage

* Thu Dec 18 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3-alt2
- Fix dir provides

* Tue Aug 05 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3-alt1
- Fix %%webserver_manualaddosndir macros name (%%webserver_manualaddosndir
  obsoleted)

* Tue Aug 05 2008 Aleksey Avdeev <solo@altlinux.ru> 1.2-alt1
- Add %%webserver_manualaddosndir dir

* Sun Jul 13 2008 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt1
- Add build subpackage for ALT Linux RPM Packaging Policy:
  + rpm-macros-%%name
  + rpm-build-%%name
- Rename macro %%webserver_webapps to %%webserver_webappsdir

* Thu Jul 10 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt4
- Add dir provides

* Tue Jul 01 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt3
- Use rpm-build-licenses

* Mon Jun 30 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt2
- Add new conflicts

* Tue Jun 10 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Add %%webserver_webapps dir (see
  http://freesource.info/wiki/AltLinux/Policy/Drafts/webpolicy)
- Conflicts update

* Mon May 14 2007 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- First build for ALT Linux
