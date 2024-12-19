using System;
using System.Diagnostics;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Threading;

namespace RAM
{
    public partial class MainWindow : Window
    {
        private DispatcherTimer _performanceUpdateTimer;

        public MainWindow()
        {
            InitializeComponent();

            // Initialize performance tracking updates
            _performanceUpdateTimer = new DispatcherTimer
            {
                Interval = TimeSpan.FromSeconds(1)
            };
            _performanceUpdateTimer.Tick += UpdatePerformanceTracking;
            _performanceUpdateTimer.Start();
        }

        // Event handler for the "Send" button
        private void SendButton_Click(object sender, RoutedEventArgs e)
        {
            string userMessage = UserInput.Text;

            // Ensure the input is not empty
            if (!string.IsNullOrWhiteSpace(userMessage))
            {
                // Display user's message in the chat history
                ChatHistory.Items.Add($"You: {userMessage}");

                // Simulate bot response
                string botResponse = GetBotResponse(userMessage);
                ChatHistory.Items.Add($"Bot: {botResponse}");

                // Clear the input field
                UserInput.Clear();
            }
        }

        // Simulated bot response logic
        private string GetBotResponse(string message)
        {
            // Placeholder bot logic
            return $"You said: {message}";
        }

        // Placeholder visibility logic
        private void UserInput_TextChanged(object sender, TextChangedEventArgs e)
        {
            Placeholder.Visibility = string.IsNullOrWhiteSpace(UserInput.Text) ? Visibility.Visible : Visibility.Hidden;
        }

        // Event handler for Hamburger Menu click
        private void HamburgerMenu_Click(object sender, RoutedEventArgs e)
        {
            ContextMenu menu = new ContextMenu();

            MenuItem settings = new MenuItem { Header = "Settings" };
            MenuItem reports = new MenuItem { Header = "Reports" };
            MenuItem about = new MenuItem { Header = "About" };
            MenuItem exit = new MenuItem { Header = "Exit" };

            settings.Click += SettingsMenu_Click;
            reports.Click += ReportsMenu_Click;
            about.Click += AboutMenu_Click;
            exit.Click += (s, args) => Application.Current.Shutdown();

            menu.Items.Add(settings);
            menu.Items.Add(reports);
            menu.Items.Add(about);
            menu.Items.Add(exit);

            menu.PlacementTarget = (Button)sender;
            menu.IsOpen = true;
        }

        // Event handler for "Settings" menu
        private void SettingsMenu_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Settings menu clicked!");
        }

        // Event handler for "Reports" menu
        private void ReportsMenu_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("Reports menu clicked!");
        }

        // Event handler for "About" menu
        private void AboutMenu_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("RAM AI - Version 1.0\nDeveloped by Your Name");
        }

        // Update performance tracking
        private void UpdatePerformanceTracking(object sender, EventArgs e)
        {
            // Example: Simulate dynamic performance values
            CPUUsage.Text = $"{new Random().Next(10, 90)}%";
            MemoryUsage.Text = $"{new Random().Next(2000, 8000)} MB";
            GPUUsage.Text = $"{new Random().Next(5, 75)}%";
        }

        // Update current target and state dynamically
        public void UpdateCurrentTarget(string targetName, string currentState, string targetIP, string domain, int scansStarted, int scansCompleted, int scansAnalyzed, bool reportReady)
        {
            TargetName.Text = targetName;
            CurrentState.Text = currentState;
            TargetIP.Text = targetIP;
            TargetDomain.Text = domain;
            ScansStarted.Text = scansStarted.ToString();
            ScansCompleted.Text = scansCompleted.ToString();
            ScansAnalyzed.Text = scansAnalyzed.ToString();
            ReportReady.Text = reportReady ? "Yes" : "No";
        }

        // Update general tracking dynamically
        public void UpdateGeneralTracking(string currentTask, int totalTargets, int totalScans, int totalReports)
        {
            CurrentTask.Text = currentTask;
            TotalTargets.Text = totalTargets.ToString();
            TotalScans.Text = totalScans.ToString();
            TotalReports.Text = totalReports.ToString();
        }
    }
}
