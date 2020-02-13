# Generated by rust2rpm
# * Tests are run in infrastructure
%bcond_with check

%global crate docopt

Name:           rust-%{crate}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Command line argument parsing

# Upstream license specification: Unlicense/MIT
License:        Unlicense or MIT
URL:            https://crates.io/crates/docopt
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(lazy_static/default) >= 1.3.0 with crate(lazy_static/default) < 2.0.0)
BuildRequires:  (crate(regex/default) >= 1.1.5 with crate(regex/default) < 2.0.0)
BuildRequires:  (crate(serde/default) >= 1.0.0 with crate(serde/default) < 2.0.0)
BuildRequires:  (crate(serde/derive) >= 1.0.0 with crate(serde/derive) < 2.0.0)
BuildRequires:  (crate(strsim/default) >= 0.9.0 with crate(strsim/default) < 0.10.0)

%global _description \
Command line argument parsing.

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license COPYING LICENSE-MIT UNLICENSE
%doc README.md
%{_bindir}/docopt-wordlist
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/docopt-wordlist.bash

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license COPYING LICENSE-MIT UNLICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
t=$(stat -c %y completions/docopt-wordlist.bash)
sed -r -i -e "s|(DOCOPT_WORDLIST_BIN=)(.+/docopt-wordlist)|\1%{_bindir}/docopt-wordlist|" completions/docopt-wordlist.bash
touch -d "$t" completions/docopt-wordlist.bash
%cargo_prep

%build
%cargo_build

%install
%cargo_install
%{__install} -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  completions/docopt-wordlist.bash

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 07 19:49:11 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Sun Apr 07 07:35:50 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-3
- Update strsim to 0.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 Josh Stone <jistone@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-3
- Run tests in infrastructure

* Sun Oct 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-2
- Bump strsim to 0.8

* Thu Aug 30 2018 Josh Stone <jistone@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.3-3
- Bump strsim to 0.7

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.3-2
- Rebuild for rust-packaging v5

* Tue Jan 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3

* Thu Nov 30 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-2
- Bump lazy_static to 1

* Thu Nov 09 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.1-1
- Initial package
