%define        _unpackaged_files_terminate_build 1
%def_enable    check
%define        gemname relaxed-rubocop

Name:          gem-relaxed-rubocop
Version:       2.5
Release:       alt1
Summary:       A relaxed style guide for RuboCop
License:       MIT
Group:         Development/Ruby
Url:           https://relaxed.ruby.style
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.0
Provides:      gem(relaxed-rubocop) = 2.5

%description
A relaxed style guide for RuboCop. Although RuboCop is an amazing tool, some of
its default rules feel overly strict. This might distract you from the helpful
messages.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md README.md
%ruby_gemspec
%ruby_gemlibdir


%changelog
* Thu Oct 30 2025 Pavel Skrylev <majioa@altlinux.org> 2.5-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
