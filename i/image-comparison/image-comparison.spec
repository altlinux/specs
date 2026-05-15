Name: image-comparison
Version: 4.5.0
Release: alt1

Summary: Library that compares 2 images with the same sizes
License: Apache-2.0
Group: Development/Java
Url: https://github.com/romankh3/image-comparison
Vcs: https://github.com/romankh3/image-comparison.git
BuildArch: noarch

Source0: https://github.com/romankh3/image-comparison/archive/v%version.tar.gz

BuildRequires: maven-local
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-default
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)

%description
Library that compares 2 images with the same sizes
and shows the differences visually by drawing rectangles.
Some parts of the image can be excluded from the comparison.
Can be used for automation qa tests.

%javadoc_package

%prep
%setup

%pom_xpath_inject "pom:plugins" "
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-jar-plugin</artifactId>
    <version>3.3.0</version>
    <configuration>
        <archive>
            <manifestEntries>
                <Automatic-Module-Name>com.github.romankh3.image.comparison</Automatic-Module-Name>
            </manifestEntries>
        </archive>
    </configuration>
</plugin>"

%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%doc --no-dereference LICENSE

%changelog
* Fri May 15 2026 Anton Meleshnikov <alton@altlinux.org> 4.5.0-alt1
- Initial build for Sisyphus.
