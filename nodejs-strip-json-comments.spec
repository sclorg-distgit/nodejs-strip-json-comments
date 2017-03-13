%{?scl:%scl_package nodejs-strip-json-comments}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-strip-json-comments
Version:    1.0.2
Release:    5%{?dist}
Summary:    Strip comments from JSON
License:    MIT
URL:        https://github.com/sindresorhus/strip-json-comments
Source:     https://github.com/sindresorhus/strip-json-comments/archive/v%{version}.tar.gz

BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
Strip comments from JSON. Lets you use comments in your JSON files!

%prep
%setup -q -n strip-json-comments-%{version}

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/strip-json-comments
cp -pr package.json strip-json-comments.js \
    %{buildroot}%{nodejs_sitelib}/strip-json-comments
install -p -D -m0755 cli.js %{buildroot}%{nodejs_sitelib}/strip-json-comments/

mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/strip-json-comments/cli.js \
    %{buildroot}%{_bindir}/strip-json-comments

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc readme.md license
%{nodejs_sitelib}/strip-json-comments
%{_bindir}/strip-json-comments

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-5
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-4
- Rebuilt with updated metapackage

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-3
- Enable scl macros, fix license macro for el6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 19 2014 Anish Patil <apatil@redhat.com> - 1.0.2-1
- Upstream has released new version

* Tue Aug 19 2014 Anish Patil <apatil@redhat.com> - 1.0.1-1
- Upstream has released new version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 4 2014 Anish Patil <apatil@redhat.com> - 0.1.3-4
- Incorporated package review comments

* Wed May 28 2014 Anish Patil <apatil@redhat.com> - 0.1.2-3
- Incorporated package review comments

* Wed May 07 2014 Anish Patil <apatil@redhat.com> - 0.1.1-2
- Incorporated package review comments

* Thu Apr 10 2014 Anish Patil <apatil@redhat.com> - 0.1.1-1
- Initial package
