%define requires_ant               ant >= 1.6.5 ant-junit >= 1.6.5 ant-trax >= 1.6.5 ant-nodeps >= 1.6.5 ant-optional >= 1.6.5
%define requires_antlr             antlr
%define requires_apache_commons    jakarta-commons-validator jakarta-commons-logging jakarta-commons-collections  jakarta-commons-digester jakarta-commons-beanutils jakarta-commons-lang jakarta-commons-fileupload jakarta-commons-io
%define requires_aspectj           aspectj
%define requires_asm               asm
%define requires_bsh               bsh
%define requires_cactus            jakarta-cactus 
%define requires_cargo             cargo          
%define requires_cglib             cglib
%define requires_dom4j             dom4j
%define requires_ecs               sh
%define requires_ehcache           ehcache
%define requires_freemarker        freemarker
%define requires_hibernate         hibernate3 hibernate3-annotations
%define requires_java              java >= 1.5
%define requires_java_devel        java-devel >= 1.5
%define requires_javamail          ant-javamail
%define requires_jboss             runawfe-jboss = 4.2.3.GA
%define requires_jcifs             jcifs
%define requires_jta               jta
%define requires_libgtk            libgtk+2
%define requires_mozilla           firefox
%define requires_nekohtml          nekohtml
%define requires_openoffice        openoffice.org
%define requires_odmg              odmg
%define requires_portal_bridges    portals-bridges-struts
%define requires_perlcgi           perl-CGI
%define requires_struts            struts struts-taglib
%define requires_struts_test       strutstestcase
%define requires_swt               eclipse-swt
%define requires_trove             gnu-trove
%define requires_xdgutils          xdg-utils
%define requires_xjavadoc          xjavadoc


%define runawfe_update_menus echo "" >/dev/null
%define runawfe_clean_menus echo "" >/dev/null

%define JBOSS_ROOT_ORIG /usr/share/runawfe-jboss
%define JBOSS_ROOT_TARGET /usr/share/runawfe-jboss
%define JBOSS_ROOT_RPM %buildroot/%JBOSS_ROOT_TARGET

%define runawfe_jboss_libs /usr/share/java/runawfe-libs

# ID for different servers
%define server_id server
%define botstation_id botstation
%define simulation_id simulation
# Prefix, used in jboss configuration (i. e. jboss/server/prefix+name)
%define jboss_cfg_prefix runawfe-
# Jboss configuration names
%define jboss_cfg_server %jboss_cfg_prefix%server_id
%define jboss_cfg_simulation %jboss_cfg_prefix%simulation_id
%define jboss_cfg_botstation %jboss_cfg_prefix%botstation_id

%define DOC_ROOT docs/guides/ru
%define DOC_WORKFLOW wfe/docs/Workflow

%define runawfe_web_port 8080

%define make_jboss_libs_links() for fileName in `ls %1`; do linkName=`echo $fileName | awk -F - '/.*-[0-9]*(\\.[0-9]*)*.jar/ {for(i=1; i<NF; i=i+1) {if (i != 1)printf "%s", "-" >>"/dev/stdout"; printf "%s", $i >>"/dev/stdout"}; printf "%s", ".jar" >>"/dev/stdout";}' ` ; if [ "$linkName" = "" ]; then linkName=`echo $fileName`; fi ; ln -sf "%1/$fileName" "%2/$linkName"; done


%define requires_ant               ant >= 1.6.5 ant-junit >= 1.6.5 ant-optional >= 1.6.5
%define requires_apache_commons    apache-commons-validator apache-commons-logging apache-commons-collections apache-commons-digester apache-commons-beanutils apache-commons-lang apache-commons-fileupload apache-commons-io
%define requires_hibernate         sh chrpath
%define requires_cargo             cargo spring2-all
%define requires_portal_bridges    sh
%define _sysconfdir_init_d	   %_sysconfdir/rc.d/init.d

Name: runawfe
Version: 3.4.2.2
Release: alt1.svn3824
Summary: RUNA WFE Workflow/BPM management system
License: LGPL
Group: Office
Url: http://sourceforge.net/projects/runawfe
Packager: Aleksey Konstantinov <kana@altlinux.org>
Source0: %{name}-%{version}.tar.gz
BuildPrereq: %requires_jboss %requires_java %requires_java_devel %requires_ant %requires_struts %requires_struts_test unzip %requires_perlcgi %requires_libgtk %requires_hibernate %requires_bsh %requires_apache_commons %requires_dom4j %requires_trove %requires_xjavadoc %requires_cactus %requires_cargo %requires_aspectj %requires_javamail

%description
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

############################   { Packages description }   #############################
############################   { runawfe-adminkit }   #############################
%package adminkit
Group: Office
BuildArch: noarch
Summary: Admin scripts for manage runawfe
Requires: %requires_jboss %requires_java
%description adminkit
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains admin scripts for manage runawfe:
script-runner.sh to deploy demo configuration (user's and processes)
ldap-importer.sh to import from LDAP server
bot-invoker.sh to invoke bots (localy on server or remote botstation)

Must be used with runawfe-server or runawfe-simulation

############################   { runawfe-botstation }   #############################
%package botstation
Group: Office
BuildArch: noarch
Summary: Runawfe remote botstation
Requires: runawfe-commonlibs = %version-%release %requires_java %requires_jboss runawfe-adminkit = %version-%release
Conflicts: runawfe-server, runawfe-simulation
%description botstation
RunaWFE_Description RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains libs and configs for runawfe remote botstation.
By default main runawfe server must be accessible on address main_wfe_server.

############################   { runawfe-client-conf }   #############################
%package client-conf
Group: Office
BuildArch: noarch
Summary: Runawfe notifier client configuration files
%description client-conf
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains runawfe notifier and client common configuration files.

############################   { runawfe-client }   #############################
%package client
Group: Office
BuildArch: noarch
Summary: Web link to runawfe server
Requires: runawfe-common = %version-%release runawfe-client-conf = %version-%release
%description client
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package add web link to runawfe server in main menu.
By default runawfe server web interface must be accessible on main_wfe_server:%runawfe_web_port

############################   { runawfe-common }   #############################
%package common
Group: Office
BuildArch: noarch
Summary: Common elements for runawfe menu support
Requires: %requires_xdgutils
%description common
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains files, needed by runawfe menus items.

############################   { runawfe-commonlibs }   #############################
%package commonlibs
Group: Office
BuildArch: noarch
Summary: Common libs for runawfe servers
Requires: %requires_antlr %requires_apache_commons %requires_asm %requires_cglib %requires_dom4j %requires_ehcache %requires_hibernate %requires_jcifs %requires_jta %requires_nekohtml %requires_odmg %requires_struts %requires_trove %requires_portal_bridges %requires_ecs %requires_freemarker
%description commonlibs
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains common libs, which used by all runawfe servers.

############################   { runawfe-doc }   #############################
%package doc
Group: Office
BuildArch: noarch
Summary: Runawfe documentation
Requires: runawfe-common = %version-%release %requires_xdgutils
%description doc
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains documentation for all runawfe components.

############################   { runawfe-gpd }   #############################
%package gpd
Group: Office
Summary: Runawfe Graphic Process Designer
Requires: %requires_java %requires_libgtk %requires_mozilla %requires_swt
%description gpd
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains runawfe graphic process designer. 
RunaGPD is eclipse based graphic tool for developing processes for RunaWFE.

############################   { runawfe-notifier }   #############################
%package notifier
Group: Office
Summary: Runawfe notifier client
Requires: runawfe-common = %version-%release runawfe-client-conf = %version-%release %requires_java %requires_mozilla %requires_swt
%description notifier
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains runawfe notifier client. It used for automatic check for new tasks.
By default, runawfe web server must be accessible at adress main_wfe_server

############################   { runawfe-server }   #############################
%package server
Group: Office
BuildArch: noarch
Summary: Runawfe server
Requires: %requires_jboss runawfe-adminkit = %version-%release runawfe-commonlibs = %version-%release %requires_java
Conflicts: runawfe-botstation, runawfe-simulation
%description server
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains libs and configs for runawfe server. 
By default runawfe server web interface accessible on port %runawfe_web_port.

############################   { runawfe-simulation }   #############################
%package simulation
Group: Office
BuildArch: noarch
Summary: Runawfe simulation server
Requires: %requires_jboss runawfe-adminkit = %version-%release %requires_java runawfe-commonlibs = %version-%release runawfe-common = %version-%release
Conflicts: runawfe-server runawfe-botstation
%description simulation
RUNA WFE is a cross-platform end user solution for business process management. It provides rich web interface with tasklist, form player, graphical process designer, bots and more

This package contains libs and configs for runawfe simulation server.
Simulation server is used for testing new process before deploying to main runawfe server.


############################   { End of packages description }   #############################

%clean
%prep
%setup -q
%build
%install

if [ "%{_arch}" = "x86_64" ]; then
  mv eclipse eclipse86
  mv eclipse64 eclipse
fi



prepareJboss(){

	rm -Rf %JBOSS_ROOT_RPM/client
	mkdir -p %JBOSS_ROOT_RPM/client
	cp -Rf %JBOSS_ROOT_ORIG/client/* %JBOSS_ROOT_RPM/client
        # For installation we need: default configuration and deploy folders.
	mkdir -p %JBOSS_ROOT_RPM/server/default/conf
	mkdir -p %JBOSS_ROOT_RPM/server/default/deploy
        cp -Rf %JBOSS_ROOT_ORIG/server/default/conf/* %JBOSS_ROOT_RPM/server/default/conf
        cp -Rf %JBOSS_ROOT_ORIG/server/default/deploy/* %JBOSS_ROOT_RPM/server/default/deploy
}

# Expected param: 1 - ant target to build jboss config; 2 - jboss configuration name
installWFEConf(){
        # install runawfe
        ant $1

	# Port 8080 is busy on ALTLinux (by control center) so start jboss server on  port 28080
	#sed "s/8080/%runawfe_web_port/" %JBOSS_ROOT_RPM/server/default/deploy/jbossweb-tomcat55.sar/server.xml > tmp_file && mv -f tmp_file %JBOSS_ROOT_RPM/server/default/deploy/jbossweb-tomcat55.sar/server.xml
	sed "s/8080/%runawfe_web_port/" %JBOSS_ROOT_RPM/server/default/deploy/http-invoker.sar/META-INF/jboss-service.xml > tmp_file && mv -f tmp_file %JBOSS_ROOT_RPM/server/default/deploy/http-invoker.sar/META-INF/jboss-service.xml

        # remove unchanged jboss files
        rm -Rf `diff %JBOSS_ROOT_RPM/server/default/conf %JBOSS_ROOT_ORIG/server/default/conf -s -r | grep -v "diff -s -r" | grep " %JBOSS_ROOT_ORIG/server/default/conf" | grep " %JBOSS_ROOT_RPM/server/default/conf" | cut -d' ' --fields=2`
        rm -Rf `diff %JBOSS_ROOT_RPM/server/default/deploy %JBOSS_ROOT_ORIG/server/default/deploy -s -r | grep -v "diff -s -r" | grep " %JBOSS_ROOT_ORIG/server/default/deploy" | grep " %JBOSS_ROOT_RPM/server/default/deploy" | cut -d' ' --fields=2`

        mkdir -p %JBOSS_ROOT_RPM/server/$2
        mv -f %JBOSS_ROOT_RPM/server/default/conf %JBOSS_ROOT_RPM/server/$2
        mv -f %JBOSS_ROOT_RPM/server/default/deploy %JBOSS_ROOT_RPM/server/$2
        mkdir %JBOSS_ROOT_RPM/server/$2/data
        cp -Rf data %JBOSS_ROOT_RPM/server/$2/
        rm -Rf %JBOSS_ROOT_RPM/bin/*.dll
}

rm -Rf %JBOSS_ROOT_RPM
# Configure build script to use jboss from RPM folder
echo "" >> build.properties
echo "jboss.home.dir=%JBOSS_ROOT_RPM" >> build.properties
echo "eclipse.home.dir=\${basedir}/../eclipse" >> build.properties
echo "" >> build.properties

prepareJboss
ant install.wfe
cd rtn
ant copy.libs
cd ..
installWFEConf install.remote.bots %jboss_cfg_botstation

prepareJboss
installWFEConf install.wfe %jboss_cfg_server

prepareJboss
installWFEConf install.simulation %jboss_cfg_simulation

rm -Rf %JBOSS_ROOT_RPM/client


############################   { install sequence for runawfe-adminkit }   #############################
pushd .


rm -Rf %JBOSS_ROOT_RPM/adminkit/lib/jbossall-client.jar && ln -s %JBOSS_ROOT_TARGET/client/jbossall-client.jar %JBOSS_ROOT_RPM/adminkit/lib/jbossall-client.jar
chmod 544 %JBOSS_ROOT_RPM/adminkit/*.sh

popd

############################   { install sequence for runawfe-botstation }   #############################
pushd .




popd

############################   { install sequence for runawfe-client-conf }   #############################
pushd .


install -d %buildroot/%_sysconfdir
cat <<EOF >%buildroot/%_sysconfdir/runawfe-client.conf
WFEServer_webaddress=localhost:%runawfe_web_port
EOF

popd

############################   { install sequence for runawfe-client }   #############################
pushd .


# Install menu-entity's
install -d %buildroot/%_datadir/pixmaps
cp wfe/resources/distr-build/icons/C_20x20_256.gif %buildroot/%_datadir/pixmaps/RunaWFE-Client.gif
cp wfe/resources/distr-build/icons/wf_C_48x128.gif %buildroot/%_datadir/pixmaps/RunaWFE-Client_48.gif

popd

############################   { install sequence for runawfe-common }   #############################
pushd .


# Install menu-entity's
install -d %buildroot%_datadir/pixmaps
cp wfe/resources/distr-build/icons/E_big_20x20_256.gif %buildroot/%_datadir/pixmaps/RunaWFE-Main.gif
cp wfe/resources/distr-build/icons/wf_Ebig_48x128.gif %buildroot/%_datadir/pixmaps/RunaWFE-Main_48.gif

# All menu related files installed here
install -d %buildroot/%_datadir/desktop-directories
cp -f wfe/resources/distr-build/rpm/common/menus/runawfe.directory %buildroot/%_datadir/desktop-directories
install -d %buildroot/%_datadir/applications
cp -Lf wfe/resources/distr-build/rpm/common/menus/*.desktop %buildroot/%_datadir/applications
sed -i 's|/usr/lib|%{_libdir}|g' %buildroot/%_datadir/applications/*
install -d %buildroot/%_sysconfdir/xdg/menus/applications-merged
cp -Lf wfe/resources/distr-build/rpm/common/menus/*.menu %buildroot/%_sysconfdir/xdg/menus/applications-merged
sed -i 's|/usr/lib|%{_libdir}|g' %buildroot/%_sysconfdir/xdg/menus/applications-merged/*

install -d %buildroot/%_sbindir
cp -Lf wfe/resources/distr-build/rpm/common/sbin/* %buildroot/%_sbindir/
sed -i 's|/usr/lib|%{_libdir}|g' %buildroot/%_sbindir/*
chmod 555 %buildroot/%_sbindir/*.sh

popd

############################   { install sequence for runawfe-commonlibs }   #############################
pushd .


mkdir -p %buildroot/%runawfe_jboss_libs
mv %JBOSS_ROOT_RPM/server/default/lib/* %buildroot/%runawfe_jboss_libs/



popd

############################   { install sequence for runawfe-doc }   #############################
pushd .


# Making documentation
install -d %buildroot%_defaultdocdir/runawfe
cp -Rf %DOC_ROOT %buildroot/%_defaultdocdir/runawfe

# Install menu-entity's
install -d %buildroot%_datadir/pixmaps
cp wfe/resources/distr-build/icons/D_20x20_256.gif %buildroot/%_datadir/pixmaps/RunaWFE-Documentation.gif
cp wfe/resources/distr-build/icons/wf_D_48x128.gif %buildroot/%_datadir/pixmaps/RunaWFE-Documentation_48.gif

popd

############################   { install sequence for runawfe-gpd }   #############################
pushd .


grep -v "win32, win32, x86" gpd/build.conf/build.properties | \
grep -v "macosx, carbon, ppc" | \
grep -v "aix, motif, ppc" | \
grep -v "hpux, motif, PA_RISC" | \
grep -v "linux, gtk, ppc" | \
grep -v "linux, gtk, x86" | \
grep -v "linux, gtk, x86_64" | \
grep -v "linux, motif, x86" | \
grep -v "solaris, gtk, sparc" | \
grep -v "configs= " | \
grep -v "solaris, motif, sparc" > test
mv test gpd/build.conf/build.properties
if [ "%{_arch}" = "i586" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
elif [ "%{_arch}" = "i486" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
elif [ "%{_arch}" = "i386" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
elif [ "%{_arch}" = "i686" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
elif [ "%{_arch}" = "pentium2" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
elif [ "%{_arch}" = "pentium3" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
elif [ "%{_arch}" = "pentium4" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
elif [ "%{_arch}" = "athlon" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
elif [ "%{_arch}" = "athlon_xp" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
elif [ "%{_arch}" = "k6" ]; then
    echo "configs=linux, gtk, x86" >> gpd/build.conf/build.properties
else 
    echo "configs=linux, gtk, x86_64" >> gpd/build.conf/build.properties
fi
cd gpd 
ant
cd ..

if [ "%{_arch}" = "i586" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
elif [ "%{_arch}" = "i486" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
elif [ "%{_arch}" = "i386" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
elif [ "%{_arch}" = "i686" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
elif [ "%{_arch}" = "pentium2" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
elif [ "%{_arch}" = "pentium3" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
elif [ "%{_arch}" = "pentium4" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
elif [ "%{_arch}" = "athlon" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
elif [ "%{_arch}" = "athlon_xp" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
elif [ "%{_arch}" = "k6" ]; then
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86.zip
else 
    unzip gpd/build/runa-gpd-dev-linux.gtk.x86_64.zip
fi

mkdir -p %buildroot%{_libdir}/RunaGPD
cd gpd-dev
mv workspace workspace_demo
rm -Rf workspace
cp -Rf * %buildroot%{_libdir}/RunaGPD/
mkdir -p %buildroot/usr/share/pixmaps
mv ../wfe/resources/distr-build/icons/e_20x20_256.gif %buildroot/usr/share/pixmaps/RunaWFE-GPD.gif

#Product Runtime Configuration File

# Delete configuration file and create them as we need
rm -Rf %buildroot%{_libdir}/RunaGPD/configuration
mkdir -p %buildroot%{_libdir}/RunaGPD/configuration
cat <<EOF >%buildroot%{_libdir}/RunaGPD/configuration/config.ini
osgi.splashPath=platform:/base/plugins/ru.runa.jbpm.ui
eclipse.product=org.jbpm.ui.RUNA
osgi.bundles=org.eclipse.equinox.common@2:start,org.eclipse.update.configurator@3:start,org.eclipse.core.runtime@start
osgi.bundles.defaultStartLevel=4
osgi.instance.area=@user.home/RunaGPD-processes
org.eclipse.swt.browser.UseWebKitGTK=true
EOF

cat <<EOF >%buildroot%{_libdir}/RunaGPD/runa-gpd.ini
-vmargs
-Xms128m
-Xmx1024m
-Dorg.eclipse.swt.browser.UseWebKitGTK=true
EOF
chmod 644 %buildroot%{_libdir}/RunaGPD/runa-gpd.ini

# No one changing default configuration
find plugins/* workspace_demo/* configuration/* -type d -print0 | xargs -0 chmod 755
find plugins/* workspace_demo/* configuration/* -type f -print0 | xargs -0 chmod 644
chmod 755 configuration plugins workspace_demo

cd ..

if [ "%{_arch}" = "i586" ]; then
    cp -Rf wfe/resources/distr-build/rpm/ALTLinux6/lib/32/*  %buildroot%{_libdir}/RunaGPD/
elif [ "%{_arch}" = "pentium3" ]; then
    cp -Rf wfe/resources/distr-build/rpm/ALTLinux6/lib/32/*  %buildroot%{_libdir}/RunaGPD/
elif [ "%{_arch}" = "pentium4" ]; then
    cp -Rf wfe/resources/distr-build/rpm/ALTLinux6/lib/32/*  %buildroot%{_libdir}/RunaGPD/
elif [ "%{_arch}" = "x86_64" ]; then
    cp -Rf wfe/resources/distr-build/rpm/ALTLinux6/lib/64/*  %buildroot%{_libdir}/RunaGPD/
    chrpath -d %buildroot%{_libdir}/RunaGPD/libcairo-swt.so
fi

popd

############################   { install sequence for runawfe-notifier }   #############################
pushd .


cd rtn
ant build
mkdir -p %buildroot%{_libdir}/RunaRTN
cp deploy/* %buildroot%{_libdir}/RunaRTN
rm -Rf %buildroot%{_libdir}/RunaRTN/*.bat %buildroot%{_libdir}/RunaRTN/*win32*
cat <<EOF  >%buildroot%{_libdir}/RunaRTN/run_alt.sh
#!/bin/sh
if [ ! -d ~/.rtn ]; then
    mkdir ~/.rtn
fi
cp %{_libdir}/RunaRTN/*.properties ~/.rtn
cd ~/.rtn
SERVER_ADDRESS=\`if [ -f ~/.runawfe-client.conf ]; then grep WFEServer_webaddress ~/.runawfe-client.conf | cut -f2- -d=; else grep WFEServer_webaddress /etc/runawfe-client.conf | cut -f 2- -d=; fi\`
sed "s/main_wfe_server/\$SERVER_ADDRESS/" application.properties > tmp.file && mv tmp.file application.properties
sed "s/main_wfe_server/\$SERVER_ADDRESS/" application_ru.properties > tmp.file && mv tmp.file application_ru.properties
SERVER_ADDRESS=\`echo \$SERVER_ADDRESS | cut -d':' -f1\`
sed "s/main_wfe_server/\$SERVER_ADDRESS/" af_delegate.properties > tmp.file && mv tmp.file af_delegate.properties

MOZ_NAME=firefox
VER=""

for fileName in \`ls %{_libdir} | grep \$MOZ_NAME\`; do 
newVer=\`echo \$fileName | awk -F - '/.*-[0-9]*(\\.[0-9]*)*/ {print \$NF}' \`
if [ "\$newVer" \> "\$VER" ]; then
    VER=\$newVer
fi
done

if [ "\$VER" != "" ]; then
    export MOZILLA_FIVE_HOME=%{_libdir}/\$MOZ_NAME-\$VER
else
    export MOZILLA_FIVE_HOME=%{_libdir}/\$MOZ_NAME
fi
export LD_LIBRARY_PATH=%{_libdir}/RunaRTN:\$MOZILLA_FIVE_HOME:\$LD_LIBRARY_PATH
EOF
cat %buildroot%{_libdir}/RunaRTN/run.sh >>%buildroot%{_libdir}/RunaRTN/run_alt.sh
mv %buildroot%{_libdir}/RunaRTN/run_alt.sh %buildroot%{_libdir}/RunaRTN/run.sh
sed "s|rtn.jar|%{_libdir}/RunaRTN/rtn.jar|" %buildroot%{_libdir}/RunaRTN/run.sh > tmp.file && mv tmp.file %buildroot%{_libdir}/RunaRTN/run.sh
sed "s|swt-gtk.jar|%{_libdir}/java/swt.jar:/usr/share/java/swt.jar|" %buildroot%{_libdir}/RunaRTN/run.sh > tmp.file && mv tmp.file %buildroot%{_libdir}/RunaRTN/run.sh
chmod 555 %buildroot%{_libdir}/RunaRTN/*.sh
sed "s/wfe_server:8080/main_wfe_server/" %buildroot%{_libdir}/RunaRTN/application.properties > %buildroot%{_libdir}/RunaRTN/tmp && mv %buildroot%{_libdir}/RunaRTN/tmp %buildroot%{_libdir}/RunaRTN/application.properties
sed "s/wfe_server:8080/main_wfe_server/" %buildroot%{_libdir}/RunaRTN/application_ru.properties > %buildroot%{_libdir}/RunaRTN/tmp && mv %buildroot%{_libdir}/RunaRTN/tmp %buildroot%{_libdir}/RunaRTN/application_ru.properties
sed "s/wfe_server/main_wfe_server/" %buildroot%{_libdir}/RunaRTN/af_delegate.properties > %buildroot%{_libdir}/RunaRTN/tmp && mv %buildroot%{_libdir}/RunaRTN/tmp %buildroot%{_libdir}/RunaRTN/af_delegate.properties
sed "s/localhost:8080/main_wfe_server/" %buildroot%{_libdir}/RunaRTN/application.properties > %buildroot%{_libdir}/RunaRTN/tmp && mv %buildroot%{_libdir}/RunaRTN/tmp %buildroot%{_libdir}/RunaRTN/application.properties
sed "s/localhost:8080/main_wfe_server/" %buildroot%{_libdir}/RunaRTN/application_ru.properties > %buildroot%{_libdir}/RunaRTN/tmp && mv %buildroot%{_libdir}/RunaRTN/tmp %buildroot%{_libdir}/RunaRTN/application_ru.properties
sed "s/localhost/main_wfe_server/" %buildroot%{_libdir}/RunaRTN/af_delegate.properties > %buildroot%{_libdir}/RunaRTN/tmp && mv %buildroot%{_libdir}/RunaRTN/tmp %buildroot%{_libdir}/RunaRTN/af_delegate.properties
cd ..

# Install menu-entity's
install -d %buildroot/%_datadir/pixmaps
cp wfe/resources/distr-build/icons/t_20x20_256.gif %buildroot/%_datadir/pixmaps/RunaWFE-TaskNotifier.gif
cp wfe/resources/distr-build/icons/wf_t_48x128.gif %buildroot/%_datadir/pixmaps/RunaWFE-TaskNotifier_48.gif

if [ "%{_arch}" = "i586" ]; then
    cp -Rf wfe/resources/distr-build/rpm/ALTLinux6/lib/32/*  %buildroot%{_libdir}/RunaRTN/
elif [ "%{_arch}" = "pentium3" ]; then
    cp -Rf wfe/resources/distr-build/rpm/ALTLinux6/lib/32/*  %buildroot%{_libdir}/RunaRTN/
elif [ "%{_arch}" = "pentium4" ]; then
    cp -Rf wfe/resources/distr-build/rpm/ALTLinux6/lib/32/*  %buildroot%{_libdir}/RunaRTN/
elif [ "%{_arch}" = "x86_64" ]; then
    cp -Rf wfe/resources/distr-build/rpm/ALTLinux6/lib/64/*  %buildroot%{_libdir}/RunaRTN/
fi

popd

############################   { install sequence for runawfe-server }   #############################
pushd .


install -d %buildroot%_sysconfdir_init_d
cp wfe/resources/distr-build/rpm/common/runawfe %buildroot/%_sysconfdir_init_d



popd

############################   { install sequence for runawfe-simulation }   #############################
pushd .


# Install menu-entity's
install -d %buildroot/%_datadir/pixmaps
cp wfe/resources/distr-build/icons/Cs_20x20_256.gif %buildroot/%_datadir/pixmaps/RunaWFE-SimClient.gif
cp wfe/resources/distr-build/icons/Si_20x20_256.gif %buildroot/%_datadir/pixmaps/RunaWFE-Simulation.gif
cp wfe/resources/distr-build/icons/wf_Cs_48x128.gif %buildroot/%_datadir/pixmaps/RunaWFE-SimClient_48.gif
cp wfe/resources/distr-build/icons/wf_Si_48x128.gif %buildroot/%_datadir/pixmaps/RunaWFE-Simulation_48.gif



popd

############################   { End of packages installation sequences }   #############################


############################   { pre/post scripts for runawfe-adminkit }   #############################

############################   { pre/post scripts for runawfe-botstation }   #############################
%post botstation

# Apply patches to jboss configuration files
cp -Ru %JBOSS_ROOT_TARGET/server/default/conf %JBOSS_ROOT_TARGET/server/%jboss_cfg_botstation
cp -Ru %JBOSS_ROOT_TARGET/server/default/deploy %JBOSS_ROOT_TARGET/server/%jboss_cfg_botstation

mkdir %JBOSS_ROOT_TARGET/server/%jboss_cfg_botstation/lib

%make_jboss_libs_links "%JBOSS_ROOT_TARGET/server/default/lib" "%JBOSS_ROOT_TARGET/server/%jboss_cfg_botstation/lib"

%make_jboss_libs_links "%runawfe_jboss_libs"  "%JBOSS_ROOT_TARGET/server/%jboss_cfg_botstation/lib"

chmod +x %_sysconfdir_init_d/runawfe
%_sysconfdir_init_d/runawfe
chkconfig --add runawfe
ln -s %_sbindir/runawfe-start-%botstation_id.sh %_sbindir/runawfe-start.sh
chmod +xxx %_sbindir/runawfe-start.sh

%preun botstation

chkconfig --del runawfe

%postun botstation

cd %JBOSS_ROOT_TARGET/server/%jboss_cfg_botstation
rm -Rf log tmp work
rm -Rf lib
cd conf && rm -Rf `ls %JBOSS_ROOT_TARGET/server/default/conf`
cd ../deploy && rm -Rf `ls %JBOSS_ROOT_TARGET/server/default/deploy`
cd ..
rm -f %_sbindir/runawfe-start.sh


############################   { pre/post scripts for runawfe-client-conf }   #############################
%post client-conf

%runawfe_update_menus

%postun client-conf

%runawfe_clean_menus


############################   { pre/post scripts for runawfe-client }   #############################
%post client

%runawfe_update_menus

%postun client

%runawfe_clean_menus


############################   { pre/post scripts for runawfe-common }   #############################
%post common

%runawfe_update_menus

%postun common

%runawfe_clean_menus


############################   { pre/post scripts for runawfe-commonlibs }   #############################
%post commonlibs



%postun commonlibs




############################   { pre/post scripts for runawfe-doc }   #############################
%post doc

%runawfe_update_menus

%postun doc

%runawfe_clean_menus


############################   { pre/post scripts for runawfe-gpd }   #############################
%post gpd

mandriva=`uname -a | grep Mandriva`
if [ "$mandriva" = "" ]; then
	rm -Rf %{_libdir}/RunaGPD/plugins/org.eclipse.swt*.jar
	ln -s -t %{_libdir}/RunaGPD/plugins %{_libdir}/eclipse/plugins/org.eclipse.swt*.jar
fi
%runawfe_update_menus

%postun gpd

%runawfe_clean_menus


############################   { pre/post scripts for runawfe-notifier }   #############################

############################   { pre/post scripts for runawfe-server }   #############################
%post server

# Apply patches to jboss configuration files
cp -Ru %JBOSS_ROOT_TARGET/server/default/conf %JBOSS_ROOT_TARGET/server/%jboss_cfg_server
cp -Ru %JBOSS_ROOT_TARGET/server/default/deploy %JBOSS_ROOT_TARGET/server/%jboss_cfg_server

mkdir %JBOSS_ROOT_TARGET/server/%jboss_cfg_server/lib

%make_jboss_libs_links "%JBOSS_ROOT_TARGET/server/default/lib" "%JBOSS_ROOT_TARGET/server/%jboss_cfg_server/lib"

%make_jboss_libs_links "%runawfe_jboss_libs"  "%JBOSS_ROOT_TARGET/server/%jboss_cfg_server/lib"

chmod +x %_sysconfdir_init_d/runawfe
chkconfig --add runawfe
ln -s %_sbindir/runawfe-start-%server_id.sh %_sbindir/runawfe-start.sh
chmod +xxx %_sbindir/runawfe-start.sh

%preun server

chkconfig --del runawfe

%postun server

cd %JBOSS_ROOT_TARGET/server/%jboss_cfg_server
rm -Rf log tmp work
rm -Rf lib
cd conf && rm -Rf `ls %JBOSS_ROOT_TARGET/server/default/conf`
cd ../deploy && rm -Rf `ls %JBOSS_ROOT_TARGET/server/default/deploy`
cd ..
rm -f %_sbindir/runawfe-start.sh


############################   { pre/post scripts for runawfe-simulation }   #############################
%post simulation

cp -Ru %JBOSS_ROOT_TARGET/server/default/conf %JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation
cp -Ru %JBOSS_ROOT_TARGET/server/default/deploy %JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation

mkdir %JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation/lib

%make_jboss_libs_links "%JBOSS_ROOT_TARGET/server/default/lib" "%JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation/lib"

%make_jboss_libs_links "%runawfe_jboss_libs"  "%JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation/lib"

cd %JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation
mkdir -p log tmp work
chmod -R 777 data log tmp work
ln -s %_sbindir/runawfe-start-%simulation_id.sh %_sbindir/runawfe-start.sh
chmod +xxx %_sbindir/runawfe-start.sh

%runawfe_update_menus

%postun simulation

cd %JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation
rm -Rf log tmp work
rm -Rf lib
cd conf && rm -Rf `ls %JBOSS_ROOT_TARGET/server/default/conf`
cd ../deploy && rm -Rf `ls %JBOSS_ROOT_TARGET/server/default/deploy`
cd ..
rm -f %_sbindir/runawfe-start.sh

%runawfe_clean_menus




%files adminkit

%JBOSS_ROOT_TARGET/adminkit
%JBOSS_ROOT_TARGET/samples
%_sbindir/runawfe-stop.sh



%files botstation

%JBOSS_ROOT_TARGET/server/%jboss_cfg_botstation/conf/*
%JBOSS_ROOT_TARGET/server/%jboss_cfg_botstation/deploy/*
%JBOSS_ROOT_TARGET/server/%jboss_cfg_botstation/data/*
%_sysconfdir_init_d/*
%_sbindir/runawfe-start-%botstation_id.sh



%files client-conf

%_datadir/pixmaps/RunaWFE-Client*.gif
%_sysconfdir/runawfe-client.conf
%_datadir/applications/runawfe-conf-client.desktop
%_sbindir/runawfe-configure.sh



%files client

%_datadir/applications/runawfe-client.desktop
%_sbindir/runawfe-webclient.sh



%files common

%_datadir/pixmaps/RunaWFE-Main*.gif
%_datadir/desktop-directories/*
%_sysconfdir/xdg/menus/applications-merged/



%files commonlibs

%runawfe_jboss_libs



%files doc

%_datadir/pixmaps/RunaWFE-Documentation*.gif
%_datadir/applications/runawfe-documentation.desktop
%_defaultdocdir/runawfe



%files gpd

%{_libdir}/RunaGPD
%_datadir/applications/runagpd.*
%_datadir/pixmaps/RunaWFE-GPD.*
%_sbindir/runagpd-start.sh



%files notifier

%{_libdir}/RunaRTN
%_datadir/pixmaps/RunaWFE-TaskNotifier*.gif
%_datadir/applications/runawfe-notifier.desktop



%files server

%JBOSS_ROOT_TARGET/server/%jboss_cfg_server/conf/*
%JBOSS_ROOT_TARGET/server/%jboss_cfg_server/deploy/*
%JBOSS_ROOT_TARGET/server/%jboss_cfg_server/data/*
%_sysconfdir_init_d/*
%_sbindir/runawfe-start-%server_id.sh





%files simulation

%_datadir/pixmaps/RunaWFE-Simulation*.gif
%_datadir/pixmaps/RunaWFE-SimClient*.gif
%JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation/conf/*
%JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation/deploy/*
%JBOSS_ROOT_TARGET/server/%jboss_cfg_simulation/data/*
%_datadir/applications/runawfe-simulator-*.desktop
%_sbindir/runawfe-start-%simulation_id.sh




%changelog
* Sun Jun 17 2012 Konstantinov Aleksey <kana@altlinux.org> 3.4.2.2-alt1.svn3824
- New release

