%define        pkgname ruby-parser

Name:          ruby-parser
Version:       3.13.0
Release:       alt1
Summary:       ruby_parser (RP) is a ruby parser written in pure ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/ruby_parser
# VCS:         https://github.com/seattlerb/ruby_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %name-%version.tar

BuildRequires(pre): rpm-build-ruby
BuildRequires: unifdef
BuildRequires: ruby-hoe
BuildRequires: ruby-sexp-processor
BuildRequires: ruby-oedipus-lex
BuildRequires: gem(racc)

%description
ruby_parser (RP) is a ruby parser written in pure ruby (utilizing
racc-which does by default use a C extension). RP's output is the same
as ParseTree's output: s-expressions using ruby's arrays and base types.


%package       doc
Summary:       Documentation files for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %{name}.


%prep
%setup

%build
%gem_build ́--pre=repackage --use=ruby_parser --alias=parser --join=bin:lib

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspecdir/ruby_parser-%version.gemspec
%ruby_gemslibdir/ruby_parser-%version
%_bindir/*

%files         doc
%ruby_gemsdocdir/ruby_parser-%version

%changelog
* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- Bump to 3.13.0
- Use setup gem's dependency detection

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 3.12.0-alt1
- Bump to 3.12.0;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.11.0-alt1
- Initial build for Sisyphus
