Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat maven-surefire-provider-junit4
Name:           xmvn
Version:        0.5.0
Release:        alt1_5jpp7
Summary:        Local Extensions for Apache Maven
License:        ASL 2.0
URL:            http://mizdebsk.fedorapeople.org/xmvn
BuildArch:      noarch
Source0:        https://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.xz

# from upstream commit ccc197d to fix NPE
Patch0:         0001-Be-careful-when-unboxing-Boolean-that-can-be-null.patch

# from upstream commits f62ca1f and f6b2c9 to fix handling of packages with dots
# in groupid
Patch1:         0002-Implement-desired-handling-dots-in-JPP-groupId.patch

# from upstream commits 44d9c60 and bf7b9a7 to allow resolution
# of tools.jar without specifying system scope or systemPath
Patch2:         0003-Implement-Java-home-resolver.patch


BuildRequires:  maven-local
BuildRequires:  beust-jcommander
BuildRequires:  cglib
BuildRequires:  guava
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-containers-container-default
BuildRequires:  plexus-utils
BuildRequires:  xbean
BuildRequires:  xml-commons-apis
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-plugin-build-helper
BuildRequires:  maven-assembly-plugin

Requires:       maven
Requires:       beust-jcommander
Requires:       guava
Requires:       plexus-classworlds
Requires:       plexus-containers-container-default
Requires:       plexus-utils
Requires:       xbean
Requires:       xml-commons-apis
Source44: import.info

%description
This package provides extensions for Apache Maven that can be used to
manage system artifact repository and use it to resolve Maven
artifacts in offline mode, as well as Maven plugins to help with
creating RPM packages containing Maven artifacts.

%package        javadoc
Group: Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description    javadoc
This package provides %{summary}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Add cglib test dependency as a workaround for rhbz#911365
%pom_add_dep cglib:cglib::test %{name}-core


# remove dependency plugin, we provide apache-maven by symlink
%pom_remove_plugin :maven-dependency-plugin
# get mavenVersion that is expected
mver=$(sed -n '/<mavenVersion>/{s/.*>\(.*\)<.*/\1/;p}' \
           xmvn-parent/pom.xml)
mkdir -p target/dependency/
ln -s %{_datadir}/maven target/dependency/apache-maven-$mver

%build
%mvn_file ":{xmvn-{core,connector}}" %{name}/@1 %{_datadir}/%{name}/lib/@1
%mvn_build -X -f

# let's use generated tarball to copy directory structure
# workaround for plexus-archiver bug
# https://github.com/sonatype/plexus-archiver/pull/9
sed -i '1s:^BZBZ:BZ:' target/*tar.bz2
tar --delay-directory-restore -xvf target/*tar.bz2
chmod -R +rwX %{name}-%{version}*


%install
%mvn_install

cp -r %{name}-%version/* %{buildroot}%{_datadir}/%{name}/
ln -sf %{_datadir}/maven/bin/mvn %{buildroot}%{_datadir}/%{name}/bin/mvn
ln -sf %{_datadir}/maven/bin/mvnDebug %{buildroot}%{_datadir}/%{name}/bin/mvnDebug
ln -sf %{_datadir}/maven/bin/mvnyjp %{buildroot}%{_datadir}/%{name}/bin/mvnyjp



# helper scripts
install -d -m 755 %{buildroot}%{_bindir}
install -m 755 xmvn-tools/src/main/bin/tool-script \
               %{buildroot}%{_datadir}/%{name}/bin/

for tool in subst resolve bisect;do
    rm %{buildroot}%{_datadir}/%{name}/bin/%{name}-$tool
    ln -s tool-script \
          %{buildroot}%{_datadir}/%{name}/bin/%{name}-$tool

    cat <<EOF >%{buildroot}%{_bindir}/%{name}-$tool
#!/bin/sh -e
exec %{_datadir}/%{name}/bin/%{name}-$tool "\${@}"
EOF
    chmod +x %{buildroot}%{_bindir}/%{name}-$tool
done

# copy over maven lib directory
cp -r %{_datadir}/maven/lib/* %{buildroot}%{_datadir}/%{name}/lib/

# possibly recreate symlinks that can be automated with xmvn-subst
%{buildroot}%{_datadir}/%{name}/bin/%{name}-subst \
        %{buildroot}%{_datadir}/%{name}/

# /usr/bin/xmvn script
cat <<EOF >%{buildroot}%{_bindir}/%{name}
#!/bin/sh -e
export M2_HOME="\${M2_HOME:-%{_datadir}/%{name}}"
exec mvn "\${@}"
EOF

# make sure our conf is identical to maven so yum won't freak out
cp -P %{_datadir}/maven/conf/settings.xml %{buildroot}%{_datadir}/%{name}/conf/

%files -f .mfiles
%doc LICENSE NOTICE
%doc AUTHORS README
%{_bindir}/*
%{_datadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Aug 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_5jpp7
- nobootstrap build

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Thu Mar 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

