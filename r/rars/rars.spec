Name: rars
Version: 1.5
Release: alt1

Summary: RISC-V Assembler and Runtime Simulator

License: MIT
Group: Emulators
Url: https://github.com/TheThirdOne/rars

Packager: Nikita Ermakov <arei@altlinux.org>

Source: %name-%version.tar
Source1: jsoftfloat.tar
Patch: %name-%version.patch

BuildRequires: java-devel-default
BuildArch: noarch
Requires: java-openjdk

%description
RARS, the RISC-V Assembler, Simulator, and Runtime, will assemble and
simulate the execution of RISC-V assembly language programs. Its
primary goal is to be an effective development environment for people
getting started with RISC-V.

%package javadoc
Group: Documentation
Summary: Javadoc for %name

%description javadoc
Documentation and license for %name.

%prep
%setup -a1
%patch -p1

%build
export LC_ALL=ru_RU.UTF-8
./build-jar.sh

%install
# jar and launcher
install -d -m 755 %{buildroot}%{_javadir}/
install -d -m 755 %{buildroot}%{_bindir}/
cp -p %name.jar %{buildroot}%{_javadir}/%name-%version.jar
ln -s %name-%version.jar %{buildroot}%{_javadir}/%name.jar
cp -p rars.sh %{buildroot}%{_bindir}/rars

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr License.txt README.md %{buildroot}%{_javadocdir}/%{name}/

%files
%_javadir/*
%_bindir/*

%files javadoc
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*

%changelog
* Wed Dec 15 2021 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Version up
- Import JSoftFloat submodule

* Tue Sep 24 2019 Nikita Ermakov <arei@altlinux.org> 1.3.1-alt1
- Initial build for ALT Linux Sisyphus.
