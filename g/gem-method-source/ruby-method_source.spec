%define        pkgname method-source
%define        gemname method_source

Name: 	       gem-%pkgname
Version:       1.0.0
Release:       alt1
Summary:       return the sourcecode for a method
License:       MIT
Group:         Development/Ruby
Url:           https://banisterfiend.wordpress.com/
Vcs:           https://github.com/banister/method_source.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Retrieve the sourcecode for a method.

NOTE: This simply utilizes Method#source_location; it does not access the live
AST.

method_source is a utility to return a method's sourcecode as a Ruby string.
Also returns Proc and Lambda sourcecode.

Method comments can also be extracted using the comment method.

It is written in pure Ruby (no C).

* Some Ruby 1.8 support now available.
* Support for MRI, RBX, JRuby, REE

method_source provides the source and comment methods to the Method and
UnboundMethod and Proc classes.


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
* Fri Jun 05 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- > Ruby Policy 2.0
- ^ 0.9.0 -> 1.0.0
- ! spec tags and syntax

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version.

* Thu Aug 23 2018 Andrey Cherepanov <cas@altlinux.org> 0.8.2-alt1.1
- Rebuild for new Ruby autorequirements.
- Disable tests.

* Wed May 17 2017 Gordeev Mikhail <obirvalger@altlinux.org> 0.8.2-alt1
- Initial build in Sisyphus
