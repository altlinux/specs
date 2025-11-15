%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: dir2txt
Version: 1.0.0
Release: alt1

Summary: A blazing-fast CLI tool to export a directory's structure and contents into a neatly formatted .txt or .json file
License: MIT
Group: File tools
Url: https://github.com/shubhamoy/dir2txt

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++

%description
Turn your entire project directory into a clean, readable, and AI-friendly
output - effortlessly. A blazing-fast CLI tool to export a directory's
structure and contents into a neatly formatted .txt or .json file.

Features:

* Generates a beautiful directory tree view
* Dumps actual file contents (optionally stripped of comments)
* Respects .gitignore, .dockerignore, and custom ignore files
* Smart binary file detection (skips them)
* Outputs in text or structured JSON - perfect for feeding into AI pipelines

%prep
%setup

%build
%cmake
%cmake_build

%install
install -pDm 755 %_cmake__builddir/dir2txt %buildroot%_bindir/%name

%files
%doc LICENSE logo.jpg README.md screenshot_dir2txt.png
%_bindir/%name

%changelog
* Sat Nov 15 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
