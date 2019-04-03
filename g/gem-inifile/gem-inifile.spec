%define        pkgname inifile

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1
Summary:       This is a native Ruby package for reading and writing INI files
License:       N/A
Group:         Development/Ruby
Url:           https://github.com/TwP/inifile
# VCS:         https://github.com/TwP/inifile.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
%summary.

Although made popular by Windows, INI files can be used on any system thanks to
their flexibility. They allow a program to store configuration data, which can
then be easily parsed and changed. Two notable systems that use the INI format
are Samba and Trac.

More information about INI files can be found on the Wikipedia Page.


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
