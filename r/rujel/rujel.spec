%define backup_dir %_localstatedir/%{name}/previous_versions/`date +%%F_%%H%%M`

Name:		rujel
Version:	0.9.3
Release:	alt1

Summary:	RUJEL is a web-portal application for maintaining online markbook in schools.
Summary(ru_RU.UTF-8): РУЖЭЛЬ — веб-приложение для ведения классного журнала.

License:	BSD
Group:		Networking/WWW
URL:		http://www.rujel.net
BuildArch: 	noarch

Packager:  	Gennady Kushnir <baywind@altlinux.org>

# http://github.com/baywind/install/
Source:		%{name}-%{version}.tar
Patch1:		%{name}-alt-config.patch

BuildRequires:	rpm-macros-webobjects
Requires: 	java >= 1.5 webobjects mysql junixsocket

Provides:	Rujel RujelDiary PListWOEditor

%description
RUJEL is a web-portal application for maintaining online markbook in
schools. It supports criterial evaluation for International
Baccalaureate schools.

RUJEL has russian user interface but it can be easily localised by
rewriting *.plist files located in Resources folder of each framework


%description -l ru_RU.UTF-8
РУЖЭЛЬ - web-приложение для ведения классного журнала.
Наиболее полно отражает подходы к ведению журнала в российской школе
и позволяет отразить всевозможные хитросплетения учебного процесса.

%prep
%setup
%patch1 -p2
echo  >> Rujel.woa/Contents/Resources/Properties
echo "RujelRevision=%release" >> Rujel.woa/Contents/Resources/Properties

echo '#!/bin/sh' > backupCron.sh
echo 'if [ -z "$1" ]' >> backupCron.sh
echo "  then exit 1" >> backupCron.sh
echo "fi" >> backupCron.sh
echo "export NEXT_ROOT=%wo_next_root" >> backupCron.sh
echo 'case $1 in' >> backupCron.sh
echo '  "day") MT=1;;' >> backupCron.sh
echo '  "week") MT=7;;' >> backupCron.sh
echo '  *) MT=31;;' >> backupCron.sh
echo "esac" >> backupCron.sh
echo 'if [ -z "`find $NEXT_ROOT/Local/Library/WebObjects/Logs/ -name Rujel?_0* -mtime -$MT`" ]' >> backupCron.sh
echo "  then exit 0" >> backupCron.sh
echo "fi" >> backupCron.sh
echo "echo >> %_localstatedir/%{name}/backup.log" >> backupCron.sh
echo 'echo `date` >> '"%_localstatedir/%{name}/backup.log" >> backupCron.sh
echo "%_datadir/%{name}/backup.sh \$1 %_localstatedir/%{name}/backup >> %_localstatedir/%{name}/backup.log"' 2>&1' >> backupCron.sh

%build

%pre

if [ "$1" != 1 ] ; then
  if [ -e %_datadir/%{name}/previous_versions ] ; then
  	mkdir -p %_localstatedir/%{name}
  	mv %_datadir/%{name}/previous_versions %_localstatedir/%{name}/
  fi

  for f in PListWOEditor Rujel RujelDiary
  do
    if [ -d %wo_appsdir/$f.woa ] ; then
      mkdir -p %backup_dir/
      mv %wo_appsdir/$f.woa %backup_dir/
      echo "mv -f %wo_appsdir/$f.woa previous/" >> %backup_dir/restore.tmp
      echo "cp -r $f.woa %wo_appsdir/" >> %backup_dir/restore.tmp
    fi
  done
  for f in Authentication Reusables RujelArchiving RujelAutoItog RujelBase RujelComplete RujelContacts RujelCriterial RujelCurriculum RujelEduPlan RujelEduResults RujelEmail RujelInterfaces RujelReports RujelSchedule RujelStats RujelUsers RujelVseLists
  do
    if [ -d %wo_frameworks/$f.framework ] ; then
      mkdir -p %backup_dir/Frameworks/
      mv %wo_frameworks/$f.framework %backup_dir/Frameworks/
      echo "mv -f %wo_frameworks/$f.framework previous/Frameworks/" >> %backup_dir/restore.tmp
      echo "cp -r Frameworks/$f.framework %wo_frameworks/" >> %backup_dir/restore.tmp
    fi
  done
  if [ -e %backup_dir/restore.tmp ] ; then
    echo "#!/bin/sh" > %backup_dir/restore.sh
    echo "mkdir  -p previous/Frameworks" >> %backup_dir/restore.sh
    cat %backup_dir/restore.tmp >> %backup_dir/restore.sh
    rm -f %backup_dir/restore.tmp
    chmod 755 %backup_dir/restore.sh
    echo "mv restore.sh previous/" >> %backup_dir/restore.sh
  fi
  tar -cj -f "%backup_dir/RujelConfig_`date +%%F`.tar.bz2" -C %wo_configdir rujel
fi


%install
# Applications
mkdir -p %buildroot%wo_appsdir
cp -r *.woa %buildroot%wo_appsdir/

# Frameworks
mkdir -p %buildroot%wo_frameworks
cp -r Frameworks/*.framework %buildroot%wo_frameworks/

# Configuration files

install -d %buildroot%wo_configdir/rujel/modules

install -m 664 -pD Configuration/logging/logging.properties %buildroot%wo_configdir/rujel/
install -m 664 -pD Configuration/logging/diaryLog.properties %buildroot%wo_configdir/rujel/
install -m 666 -pD Configuration/message.txt %buildroot%wo_configdir/rujel/

cp -r Configuration/RUJELsetup %buildroot%wo_configdir/
cp -r Configuration/RujelReports %buildroot%wo_configdir/rujel/

install -m 640 -pD Configuration/SiteConfig.xml %buildroot%_datadir/%{name}/SiteConfig.xml

#data
install -d -m 750 %buildroot%_datadir/%{name}/complete/students
install -d -m 755 %buildroot%_datadir/%{name}/complete/courses

cp -r SQL %buildroot%_datadir/%{name}/

#backup scripts
install -m 755 backup.sh %buildroot%_datadir/%{name}/
install -m 755 backupCron.sh %buildroot%_datadir/%{name}/
install -d -m 755 %buildroot%_localstatedir/%{name}/backup



%post
cd %wo_appsdir
for f in *.woa; do
  if [ -d $f/Contents/WebServerResources ] ; then
    mkdir -p %wo_web_resources/$f/Contents/
    ln -fns %wo_appsdir/$f/Contents/WebServerResources %wo_web_resources/$f/Contents/WebServerResources
  fi
done

cd %wo_frameworks
for f in *.framework; do
  if [ -d $f/WebServerResources ] ; then
    mkdir -p %wo_web_resources/Frameworks/$f
    ln -fns  %wo_frameworks/$f/WebServerResources %wo_web_resources/Frameworks/$f/WebServerResources
  fi
done

ln -fns %_datadir/java/junixsocket/junixsocket.jar %wo_localroot/Library/WebObjects/Extensions
ln -fns %_datadir/java/junixsocket/junixsocket-mysql.jar %wo_localroot/Library/WebObjects/Extensions

if [ "$1" = 1 ] ; then
  grep -iq "rujel" %wo_configdir/SiteConfig.xml > /dev/null 2>&1 ||
    install -b -pD -m 640 --owner=%wo_user --group=%wo_group %_datadir/%{name}/SiteConfig.xml %wo_configdir/

  if [ ! -e %wo_configdir/rujel/rujel.plist ] ; then
    cp %wo_configdir/RUJELsetup/required/* %wo_configdir/rujel/modules/
    cp %wo_configdir/RUJELsetup/recommended/* %wo_configdir/rujel/modules/
    cp %wo_configdir/RUJELsetup/dbpresets/MySQL_junixsocket.plist %wo_configdir/rujel/modules/database.plist
    chown -R %wo_user:%wo_group %wo_configdir/rujel/modules/
    mv %wo_configdir/rujel/modules/rujel.plist %wo_configdir/rujel/
  fi
  %post_service wotaskd
  %post_service womonitor
fi

if ! grep -iq "rujel" %_sysconfdir/crontab ; then
  echo >> %_sysconfdir/crontab
  echo "## backup Rujel databases" >> %_sysconfdir/crontab
  echo "05 5 1 * * %wo_user %_datadir/%{name}/backupCron.sh all" >> %_sysconfdir/crontab
  echo "05 5 2-31 * * %wo_user %_datadir/%{name}/backupCron.sh day" >> %_sysconfdir/crontab
  echo "03 5 * * 0 %wo_user %_datadir/%{name}/backupCron.sh week" >> %_sysconfdir/crontab
  %post_service crond
fi

#%_datadir/%{name}/backupCron.sh all

%preun
if [ "$1" = 0 ] ; then
  rm -rf %_datadir/%{name}/previous_versions

  for f in PListWOEditor Rujel RujelDiary
  do
    if [ -d %wo_web_resources/$f.woa ] ; then
      rm -rf %wo_web_resources/$f.woa
    fi
  done
  for f in Authentication Reusables RujelArchiving RujelAutoItog RujelBase RujelComplete RujelContacts RujelCriterial RujelCurriculum RujelEduPlan RujelEduResults RujelEmail RujelInterfaces RujelReports RujelSchedule RujelStats RujelUsers RujelVseLists
  do
    if [ -d %wo_web_resources/Frameworks/$f.framework ] ; then
     rm -rf %wo_web_resources/Frameworks/$f.framework
    fi
  done
fi

%files
%defattr(-,%wo_user,%wo_group)
%wo_appsdir/*
%wo_frameworks/*
%_datadir/%{name}
%_localstatedir/%{name}
%wo_configdir/RUJELsetup
%config(noreplace) %wo_configdir/rujel
%exclude %wo_configdir/rujel/RujelReports
%config %wo_configdir/rujel/RujelReports

%changelog
* Sat Jan 07 2012 Gennady Kushnir <baywind@altlinux.org> 0.9.3-alt1
- upstream update (88570546...)
- install script changed
* Wed Nov 09 2011 Gennady Kushnir <baywind@altlinux.org> 0.9.1-alt4
- upstream update (a7bd4196...)
* Tue Oct 11 2011 Gennady Kushnir <baywind@altlinux.org> 0.9.1-alt3
- upstream update (f2fef036...)
* Wed Sep 21 2011 Gennady Kushnir <baywind@altlinux.org> 0.9.1-alt2
- upstream update (f487552b...)
* Thu Aug 04 2011 Gennady Kushnir <baywind@altlinux.org> 0.9.1-alt1
- upstream update (46383c57...)
* Fri Jun 17 2011 Gennady Kushnir <baywind@altlinux.org> 0.9.0-alt2
- upstream update (321cf6a3...)
* Tue May 31 2011 Gennady Kushnir <baywind@altlinux.org> 0.9.0-alt1
- upstream update (7a6f7213...)
* Fri Dec 17 2010 Gennady Kushnir <baywind@altlinux.org> 0.8.9-alt5
- upstream update (0ce2a9e0...)
* Tue Dec 14 2010 Gennady Kushnir <baywind@altlinux.org> 0.8.9-alt4
- upstream update (eb9895bb...)
- fixed first run %%post script
* Mon Dec 13 2010 Gennady Kushnir <baywind@altlinux.org> 0.8.9-alt3
- fixed LDAP connection issue
- upstream update (682fab99...)
* Sun Dec 12 2010 Gennady Kushnir <baywind@altlinux.org> 0.8.9-alt2
- upstream update (8924c5ed...)
- added message.txt
* Sun Nov 21 2010 Gennady Kushnir <baywind@altlinux.org> 0.8.9-alt1
- upstream update (76d9e477...)
- auto-writing release info into Properties
- working minimal initial configuration
* Thu Nov 07 2010 Gennady Kushnir <baywind@altlinux.org> 0.8.8-alt3
- upstream update (ba70d2dc...)
* Thu Oct 14 2010 Gennady Kushnir <baywind@altlinux.org> 0.8.8-alt2
- upstream update (1c474c61...)
* Thu Oct 07 2010 Gennady Kushnir <baywind@altlinux.org> 0.8.8-alt1
- upstream update (17114e75...)
- using patch instead of subst in %%prep
* Wed Sep 22 2010 Gennady Kushnir <baywind@altlinux.org> 0.8.7-alt1
- Initial release
