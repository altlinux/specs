%define _unpackaged_files_terminate_build 1
%define  pkgname deckar01-task_list

Name: gem-%pkgname
Version: 2.3.2
Release: alt1

Summary: Markdown Task List feature components 
License: MIT
Group: Development/Ruby
Url: https://github.com/deckar01/task_list
VCS: https://github.com/deckar01/task_list
BuildArch: noarch

Source: %pkgname-%version.tar

BuildRequires(pre): rpm-macros-ruby
BuildRequires: rpm-build-ruby

%description
The Task List feature is made of several different components:
- Markdown Ruby Filter
- Summary Ruby Model: summarizes task list items
- JavaScript: frontend task list update behavior
- CSS: styles Markdown task list items

%package doc
Summary: Documentation files for %name gem
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc *.md
%ruby_gemspec
%ruby_gemlibdir

%files doc
%ruby_gemdocdir

%changelog
* Tue Apr 28 2026 Aleksandr Dovydenkov <asd@altlinux.org> 2.3.2-alt1
- Initial build for ALT Linux.
