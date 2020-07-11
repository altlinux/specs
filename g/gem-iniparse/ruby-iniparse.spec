%define        pkgname iniparse

Name:          gem-%pkgname
Version:       1.5.0
Release:       alt1
Summary:       IniParse is a pure Ruby library for parsing INI configuration and data files.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/antw/iniparse
Vcs:           https://github.com/antw/iniparse.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.

Main features:

* Support for duplicate options. While not common, some INI files contain an
  option more than once. IniParse does not overwrite previous options, but
  allows you to access all of the duplicate values.
* Preservation of white space and blank lines. When writing back to your INI
  file, line indents, white space and comments (and their indents) are
  preserved. Only trailing white space (which has no significance in INI files)
  will be removed.
* Preservation of section and option ordering. Sections and options are kept in
  the same order they are in the original document ensuring that nothing gets
  mangled when writing back to the file.

If you don't need the above mentioned features, you may find the simpler IniFile
gem does all you need.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- > Ruby Policy 2.0
- ^ 1.4.4 -> 1.5.0
- ! spec tags

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1.1
- Rebuild for new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.4.4-alt1
- Initial build for Sisyphus
