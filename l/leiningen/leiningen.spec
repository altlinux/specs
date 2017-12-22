%define write_group users

Name:           leiningen
Version:        2.8.1
Release:        alt2
Summary:        Leiningen is for automating Clojure projects without setting your hair on fire

Group:          Development/Java
License:        Eclipse Public License
URL:            https://leiningen.org/
Source0:        %name-%version.tar
Source1:        leiningen-%version-standalone.zip
Source2:	repository.tar
Source3: 	lein-classpath
Patch1:         alt-lein-use-offline-repo.patch

BuildRequires(pre): rpm-build-java
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  /proc
BuildRequires:  clojure

BuildArch:      noarch
Requires:       clojure

%description
Leiningen is the easiest way to use Clojure. With a focus on project
automation and declarative configuration, it gets out of your way and
lets you focus on your code.

%prep
%setup
%patch1 -p1

%install
install -Dpm 755 bin/lein %buildroot%_bindir/lein
install -Dpm 644 %SOURCE1 \
                 %buildroot%_javadir/leiningen/leiningen-%version-standalone.jar
install -Dpm 644 %SOURCE3 \
                 %buildroot%_javadir/leiningen/.m2/.lein-classpath
tar xf %SOURCE2 -C %buildroot%_javadir/leiningen

# Symlinks all directories with jar
find %buildroot%_javadir/leiningen/.m2/repository/ -name \*.jar | sed 's,^.*/.m2/repository/\(.*\)/.*$,\1,' | while read dir
do
	mkdir -p %buildroot%_localstatedir/%name/.m2/repository/$dir
	ln -rs "%buildroot%_javadir/leiningen/.m2/repository/$dir" "%buildroot%_localstatedir/%name/.m2/repository/$dir"
done
cp -a %buildroot%_javadir/leiningen/.m2/.lein-classpath %buildroot%_localstatedir/%name/.m2/.lein-classpath

# Make writeable pathes
find %buildroot%_localstatedir/%name/.m2/repository -type d | sed 's|%buildroot|%%attr(775,root,%write_group) |' > writeable_files

%files -f writeable_files
%doc *.md
%_bindir/lein
%_javadir/%name
%dir %_localstatedir/%name
%dir %_localstatedir/%name/.m2
%attr(775,root,%write_group) %config(noreplace) %_localstatedir/%name/.m2/.lein-classpath

%changelog
* Fri Dec 15 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt2
- Fix repository directories and config file permissions.
- Spec cleanup.

* Wed Nov 29 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- Initial build in Sisyphus
